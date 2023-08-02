from helper import *
import os
from astropy.time import Time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rfi_query.settings')
from django.core.wsgi import get_wsgi_application
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()
from rfi.models import *
import glob
# Frequency,Source,Polarization,File,Project,FrequencyType,Session

print('Creating Dataframe')

f_path = '/Users/clive/codes/NRAO/gbt-rfi-gui/RFI_VLA_Sample_Merged'
files = glob.glob(f'{f_path}/*')

# f = File(path=f_path,name=f_path.split('/')[-1])
# f.save()

pr = Project(name=f_path.split('/')[-2])
pr.save()

df_records = pd.read_csv(files[0])
df_records = df_records.to_dict('records')
datetime = f'{df_records[0]["OBS. DATE"]} {df_records[0]["Time of record"]}'
t = Time(datetime,format='iso')
mjd = t.mjd
source = df_records[0]["Source"]

s = Source(name=source)
s.save()

polarization = ['LL','RR']
model_instances1 = [Polarization(name=polar) for polar in polarization]
p = Polarization.objects.bulk_create(model_instances1,ignore_conflicts=True)

bands = ['A','C','K','L','P','Q','S','U','X']
model_instances2 = [FrequencyType(name=band) for band in bands]
ft = FrequencyType.objects.bulk_create(model_instances2)
ft_name = [i.name for i in ft]

model_instances3 = [Frontend(name=f'{band}_Band_Reciever') for band in bands]
front = Frontend.objects.bulk_create(model_instances3)


counter = 1
for file in files:
    df_records = pd.read_csv(file)
    df_records = df_records.to_dict('records')
    polarization = df_records[0]["Polar"]
    ftype = f"{file.split('/')[-1].split('_')[0]}"
    print('Inserting Values to model')

    f = File(path=file,name=file.split('/')[-1])
    f.save()



    ses = Session(name=counter,project=pr,file=f)
    ses.save()
    if polarization == 'LL':
        if ftype in ft_name:
            scan = Scan(session = ses,source=s,frequency_type=ft[ft_name.index(ftype)],
                        polarization=p[0],mjd=mjd,datetime=datetime,frontend=front[ft_name.index(ftype)])
    
    else:
        if ftype in ft_name:
            print(front[ft_name.index(ftype)])
            scan = Scan(session = ses,source=s,frequency_type=ft[ft_name.index(ftype)],
                polarization=p[1],mjd=mjd,datetime=datetime,frontend = front[ft_name.index(ftype)])
    scan.save()


    model_instances = [Frequency(
        frequency=record['Frequency'],scan=scan,
        intensity=record['Ampl(Jy)']
    ) for record in df_records]


    Frequency.objects.bulk_create(model_instances)
    counter+=1
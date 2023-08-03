import pandas as pd
import re

def extract_datetime(df):
    date = df['OBS. DATE'][0]
    time = df['Time of record'][0]

    year = date[1:5]
    month = date[5:7]
    day = date[7:]

    _,hr,min,sec = time.split()
    return year,month,day,hr,min,sec


def read_txt(file):
    with open(file) as f:
        contents = f.readlines()

    data = []
    header = []
    info = []
    for i,content in enumerate(contents):
        if 'Channel' in content:
            header.append(content)
            data_index = i

        elif len(header) != 0:
            data.append(content)
        
        else:
            if ' \n'  == content:
                pass
            else:
                info.append(content)
    return data,header,info


def txt_to_df(file):
    vals = []
    to_extract = ['Source' , 'RA' , 'DEC' , 'OBS. DATE' , 'No. channels' , 'Bw (kHz)','Time of record']

    data,header,info = read_txt(file)

    for i,_ in enumerate(info):
        info[i] = info[i].split('\n')[0].split(':')
    info = info[1:-1]


    info_flat = []
    for i,k in enumerate(info):
        for j, _ in enumerate(k):
            if '        ' or '   'in info[i][j]:

                info[i][j] = re.split(r'     |   ',info[i][j])
                # info[i][j] = info[i][j].split('     ')
                info_flat += (info[i][j])
            else:
                info_flat.append(info[i][j])

    info_flat = list(filter(None,info_flat))
    header = header[0].split('\n')[0].split()

    for i,k in enumerate(data):
        data[i] = data[i].split('\n')[0].split()

    for _,l in enumerate(to_extract):
        if l in info_flat:
            index = info_flat.index(l)
            # print(l)
            vals.append(info_flat[index+1])


    df = pd.DataFrame(data=data,columns=header)
    df[to_extract] = vals

    year,month,day,hr,min,sec = extract_datetime(df)

    for i,k in enumerate(df['OBS. DATE']):
        df['OBS. DATE'][i] = pd.to_datetime(f'{year}-{month}-{day}')
        df['Time of record'] = f'{hr}:{min}:{sec}'
    
    print('Done Creating Dataframe')
    df_records = df.to_dict('records')

    return df_records

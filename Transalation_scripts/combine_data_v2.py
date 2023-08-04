import glob
import os
from helper import *

bands = ['A','C','K','L','P','Q','S','U','X']
folders = glob.glob(f'RFI_VLA_Sample/*')

for folder in folders:
    date = folder.split('/')[-1]
    print(date)
    for band in bands:
        file_path = f'RFI_VLA_Sample_Merged/{band}_RR_merged_{date}.csv'

        if not os.path.exists(file_path):
            files = glob.glob(f'{folder}/{band}*')
            try:
            # print(band)
                files = sorted(files,key=lambda x: int(x.split('/')[-1].split('.')[0].split(f'{band}')[1]))
            except:
                pass

            LL = [file for file in files if file.split('.')[1] == 'LL']
            RR = [file for file in files if file.split('.')[1] == 'RR']


            df_record_LL = []
            df_record_RR = []

            for i in range(len(LL)):
                df_record_LL.append(pd.DataFrame.from_dict(txt_to_df(LL[i])));
                df_record_RR.append(pd.DataFrame.from_dict(txt_to_df(RR[i])));

            # print(df_record_LL[0].head())
            # print(df_record_RR[0].head())

            merged_df_LL = pd.concat(df_record_LL)
            merged_df_RR = pd.concat(df_record_RR)

            merged_df_sorted_LL = merged_df_LL.sort_values('Ampl(Jy)', ascending=False).drop_duplicates('Frequency').sort_index()
            merged_df_sorted_LL = merged_df_sorted_LL.sort_values('Frequency')
            merged_df_sorted_LL.to_csv(f'RFI_VLA_Sample_Merged/{band}_LL_merged_{date}.csv')

            merged_df_sorted_RR = merged_df_RR.sort_values('Ampl(Jy)', ascending=False).drop_duplicates('Frequency').sort_index()
            merged_df_sorted_RR = merged_df_sorted_RR.sort_values('Frequency')
            merged_df_sorted_RR.to_csv(f'RFI_VLA_Sample_Merged/{band}_RR_merged_{date}.csv')
        else:
            print(f'File:{band}_RR/LL_merged_{date}.csv already exist')
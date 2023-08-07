# VLA-RFI-GUI

## This is a fork of GBT-RFI-GUI : https://github.com/GreenBankObservatory/gbt-rfi-gui
--------------

VLA RFI GUI is a  application that is used to view RFI from monthly RFI scans of the VLA.

## Running in AOC cluster
This GUI is already setup in the aoc cluster and can be launched by the following command

```
bash /home/vla/RFI_GUI/vla_rfi_gui.sh
```

One can add this as an function in their ~/.basrc to call the GUI directly.

## Setting up in your local system:

1. Clone the repo
2. It is advised to create a virtual env before you download the nesscarry modules
3. Run the following code
   ```
   cd VLA-RFI_GUI
   pip install -r Transaltion_scripts/requirements.txt
   pip install -U pip setuptools wheel build
   pip install -e .
   ```
4. Now before inerting data to a sqlite3 database, we should create an empty database.
   ```
   python manage.py migrate
   ```
5. Before adding data to the database, put the VLA RFI.txt file in a folder named RFI_VLA_SAMPLE (change the name but make sure to update
the combine_data_v2.py and df_sql_v4.py). The structre of the folder is shown below.
  ``` bash
RFI_VLA_Sample
├── 2022_03
│   ├── A1.LL.TXT
│   ├── A1.RR.TXT
│   ├── A10.LL.TXT
│   ├── A10.RR.TXT
│   ├── A11.LL.TXT
│   ├── A11.RR.TXT
│   ├── A12.LL.TXT
│   ├── A12.RR.TXT
│   ├── A13.LL.TXT
│   ├── A13.RR.TXT
│   ├── A14.LL.TXT
│   ├── A14.RR.TXT
│   ├── A2.LL.TXT
│   ├── A2.RR.TXT
```
6. Now run `python combine_data_v2.py` and this could create a merged data. The structure of RFI_VLA_Sample_Merged is as follows
   ``` bash
   RFI_VLA_Sample_Merged
    ├── A_LL_merged_2022_03.csv
    ├── A_LL_merged_2022_08.csv
    ├── A_LL_merged_2022_11.csv
    ├── A_LL_merged_2023_02.csv
    ├── A_RR_merged_2022_03.csv
    ├── A_RR_merged_2022_08.csv
    ├── A_RR_merged_2022_11.csv
    ├── A_RR_merged_2023_02.csv
    ├── C_LL_merged_2022_03.csv
   ```
7. Now for insterting the .csv to the database, go one folder back and run `python df_sql_v4.py` and this should add all the data to db.sqlite3 which
can be found in the parent folder.

8. Now from the parent folder run `python gbt_rfi_gui/gbt_rfi_gui.py' to open up the VLA-RFI-GUI.
   <img width="600" alt="image" src="https://github.com/CliveKBinu/VLA-RFI-GUI/assets/63173077/0b13d4f1-c5e2-44e2-b730-3dd18a4aefa0">

   

### This is the original code in its original location
### THIS IS THE FINAL WORKING CODE
### Good job dude, you should have been counting the hours you spend on this thing, it was way too many.
import pandas as pd
import numpy as np
import os as os

code_file_path = os.getcwd()
print("THIS IT?:", code_file_path)

database_folder_path = (f'{code_file_path}\\database') ###FIGURE OUT HOW TO CREATE FILE PATHS TO WHERE THE PROGRAM IS LOCATED SO THE CODE DOESNT HAVE TO BE CHANGED FOR EACH NEW LOCATION
master_folder_path = (f'{code_file_path}')


df_database = pd.DataFrame()
database_files = os.listdir(database_folder_path)


df_master = pd.DataFrame()
master_file = os.listdir(master_folder_path)


df = pd.DataFrame()



for file in database_files:
    if file.endswith(".xlsx"):
        excel_database = pd.ExcelFile(f'{database_folder_path}/{file}')
        sheets = excel_database.sheet_names
        for sheet in sheets:
            df = excel_database.parse(sheet_name = sheet)
            df_database = df_database.append(df)

for file in master_file:
    if file == "NewIDRD.xlsx": ### FIGURE OUT HOW TO MAKE THE FILE IT SELECTS MORE ARBRITRARY. USE FILE.ENDSWITH(".XLSX") AND IS THE NEWEST FILE IN THE FOLDER AND =! "Missing Data".
        excel_master = pd.ExcelFile(f'{master_folder_path}/{file}')
        sheets = excel_master.sheet_names
        for sheet in sheets:
            df = excel_master.parse(sheet_name = sheet)
            df_master = df_master.append(df)
            

df_database.rename(columns={'Unnamed: 11':'Part_Number','Unnamed: 13':'Eng_Part_Name'},
inplace=True)
df_master.rename(columns={'Unnamed: 11':'Part_Number','Unnamed: 13':'Eng_Part_Name'},
inplace=True)


df_database = df_database.drop(labels=[
             'Unnamed: 0' ,'Unnamed: 1' ,'Unnamed: 2' ,'Unnamed: 3' ,'Unnamed: 4' ,'Unnamed: 5' ,'Unnamed: 6' ,'Unnamed: 7' ,'Unnamed: 8' ,'Unnamed: 9', 'Unnamed: 10','Unnamed: 12'
            ,'Unnamed: 14','Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21','Unnamed: 22','Unnamed: 23'
            ,'Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33'
            ,'Unnamed: 34','Unnamed: 35','Unnamed: 36'], axis=1)

df_master = df_master.drop(labels=[
             'Unnamed: 0' ,'Unnamed: 1' ,'Unnamed: 2' ,'Unnamed: 3' ,'Unnamed: 4' ,'Unnamed: 5','Unnamed: 6' ,'Unnamed: 6' ,'Unnamed: 7' ,'Unnamed: 8','Unnamed: 9', 'Unnamed: 10','Unnamed: 12'
            ,'Unnamed: 14','Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21','Unnamed: 22','Unnamed: 23'
            ,'Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32','Unnamed: 33'
            ,'Unnamed: 34','Unnamed: 35','Unnamed: 36'], axis=1)


strip_database = df_database.select_dtypes(['object']).columns
df_database[strip_database] = df_database[strip_database].apply(lambda x: x.str.strip())

strip_master = df_master.select_dtypes(['object']).columns
df_master[strip_master] = df_master[strip_master].apply(lambda x: x.str.strip())





df_master = df_master.merge(df_database, how='outer', indicator = True).query('_merge == "left_only"').drop('_merge',1)

df_master.to_excel (f'{master_folder_path}/Data in Master File, not covered in database.xlsx')




df_master.merge(df_database, how='outer', indicator = True).query('_merge == "left_only"').drop('_merge',1) ###This line is the data merging moneymaker

#print(df_master)


### Same Script


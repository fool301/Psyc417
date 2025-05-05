import pandas as pd
import os

file_path = '/Users/fool/Desktop/Edtpa data/All 2019 _2020 Scores for Data Analysis.xlsx'
df = pd.read_excel(file_path)

# Drop columns 4-8 
df.drop(df.columns[3:8], axis=1, inplace=True)

# Combine First_Name and Last_Name into Full_Name
df['Full_Name'] = df['First_Name'] + ' ' + df['Last_Name']

# Drop First_Name, Last_Name, and Middle Initial
df.drop(['First_Name', 'Last_Name', 'Middle_Initial'], axis=1, inplace=True, errors='ignore')

# Move Full_Name to the front
cols = ['Full_Name'] + [col for col in df.columns if col != 'Full_Name']
df = df[cols]

# Remove empty rows
df.dropna(how='all', inplace=True)

# Remove rows where Full_Name looks like a date
def is_date(string):
    try:
        pd.to_datetime(string)
        return True
    except:
        return False

df = df[~df['Full_Name'].apply(is_date)]
df = df.rename(columns={'test_code': 'Test Code'})
df['Year'] = '19/20'

# Reset index
df.reset_index(drop=True, inplace=True)

save_folder = '/Users/fool/Desktop/Edtpa data/cleaned/'
os.makedirs(save_folder, exist_ok=True)
df.to_excel(os.path.join(save_folder, 'cleaned_19-20.xlsx'), index=False)

# Print first few rows
print(df.head())

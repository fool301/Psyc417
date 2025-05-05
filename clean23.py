import pandas as pd
import os

file_path = '/Users/fool/Desktop/Edtpa data/All 2023_2024 Scores For Data Analysis.xlsx'
df = pd.read_excel(file_path)

#Drop unwanted columns
cols_to_drop = ['COORD', 'NUM', 'REGISTER', 'SUBMIT', 'EDTPA', 16, 17, 18]
df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

# Rename columns 01 to 15 --> R1 to R15
rename_dict = {i: f'R{i}' for i in range(1, 16)}
df.rename(columns=rename_dict, inplace=True)

# Combine FIRST and LAST into Full_Name
df['Full_Name'] = df['FIRST'] + ' ' + df['LAST']

# Drop FIRST and LAST columns
df.drop(columns=['FIRST', 'LAST'], inplace=True, errors='ignore')

# Move Full_Name to the FIRST column
cols = ['Full_Name'] + [col for col in df.columns if col != 'Full_Name']
df = df[cols]

# rename portfolio to column
df = df.rename(columns={'PORTFOLIO': 'Test Code'})
df['Year'] = '23/24'

# Reset index
df.reset_index(drop=True, inplace=True)

save_folder = '/Users/fool/Desktop/Edtpa data/cleaned/'
os.makedirs(save_folder, exist_ok=True)
df.to_excel(os.path.join(save_folder, 'cleaned_23-24.xlsx'), index=False)

print(df.head())
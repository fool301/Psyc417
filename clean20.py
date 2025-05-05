import pandas as pd
import os
import re

file_path = '/Users/fool/Desktop/Edtpa data/All 2020_2021 Scores For Data Analysis.xlsx'
df = pd.read_excel(file_path)

# Drop unwanted columns
cols_to_drop = ['Test Version', 'Test Name', 'Test Date', 'Total Score', 'Rubric Key Code', '16', '17', '18']
df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

# Rename columns '01' to '15' --> 'R1' to 'R15'
rename_dict = {f'{i:02d}': f'R{i}' for i in range(1, 16)}
df.rename(columns=rename_dict, inplace=True)

# Clean 'Examinee Name / SSN'
def clean_name(name):
    if pd.isna(name):
        return name
    # Remove SSN 
    name = re.sub(r'\s*\(.*?\)', '', name).strip()
    # Flip from Last, First to First Last
    if ',' in name:
        last, first = name.split(',', 1)
        return first.strip() + ' ' + last.strip()
    else:
        return name.strip()

df['Examinee Name / SSN'] = df['Examinee Name / SSN'].apply(clean_name)

df['Year'] = '20/21'

# Rename to Full_Name
df.rename(columns={'Examinee Name / SSN': 'Full_Name'}, inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

save_folder = '/Users/fool/Desktop/Edtpa data/cleaned/'
os.makedirs(save_folder, exist_ok=True)
df.to_excel(os.path.join(save_folder, 'cleaned_20-21.xlsx'), index=False)

# Print first few rows
print(df.head())

import pandas as pd
import os

# Folder where your cleaned files are saved
folder_path = '/Users/fool/Desktop/Edtpa data/cleaned'

# List of the filenames
file_names = [
    'cleaned_19-20.xlsx',
    'cleaned_20-21.xlsx',
    'cleaned_21-22.xlsx',
    'cleaned_22-23.xlsx',
    'cleaned_23-24.xlsx'
]


file_paths = [os.path.join(folder_path, file) for file in file_names]

# combine 
dfs = [pd.read_excel(file) for file in file_paths]
combined_df = pd.concat(dfs, ignore_index=True)

# Convert R1-R15 to numeric
for col in [f'R{i}' for i in range(1, 16)]:
    combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')

# Drop any rows where R1-R15 have NaN 
combined_df.dropna(subset=[f'R{i}' for i in range(1, 16)], inplace=True)

#delete names for confidentialy purposes
combined_df = combined_df.drop(columns=["Full_Name"])

# Reset index
combined_df.reset_index(drop=True, inplace=True)

save_path = os.path.join(folder_path, 'combined_all_years.xlsx')
combined_df.to_excel(save_path, index=False)

print(f"saved to: {save_path}")
print(combined_df.head())

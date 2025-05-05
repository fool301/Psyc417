import pandas as pd

# Load your file
file_path = '/Users/fool/Desktop/Edtpa data/cleaned/combined_all_years_with_program.xlsx'
df = pd.read_excel(file_path)

df = df[df['Program'].map(df['Program'].value_counts()) >= 13]

# rubric columns
rubric_cols = [f'R{i}' for i in range(1, 16)]

# Calc Total Score
df['Total Score'] = df[rubric_cols].sum(axis=1)
df = df.drop(columns=["Test Code"])


# Move Total Score right after R15
cols = list(df.columns)
r15_index = cols.index('R15')

new_order = cols[:r15_index + 1] + ['Total Score'] + cols[r15_index + 1:-1]  # -1 removes duplicate 'Total Score' at end
df = df[new_order]

print(df.head())

df.to_excel('/Users/fool/Desktop/Edtpa data/cleaned/final_data.xlsx', index=False)

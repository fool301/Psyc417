import pandas as pd

#program key file
program_df = pd.read_excel('/Users/fool/Desktop/Edtpa data/Program IDs.xlsx')
combined_df = pd.read_excel('/Users/fool/Desktop/Edtpa data/cleaned/combined_all_years.xlsx')
print(program_df.columns)


# Merge combined_df  with program_df using test code
combined_df = combined_df.merge(program_df, on='Test Code', how='left')

combined_df.to_excel('/Users/fool/Desktop/Edtpa data/cleaned/combined_all_years_with_program.xlsx', index=False)

print(combined_df.head())

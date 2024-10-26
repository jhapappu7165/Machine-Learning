import pandas as pd

df1 = pd.read_csv('new_file1.csv')
df2 = pd.read_csv('new_file2.csv')

combined_df = pd.concat([df1, df2])
combined_df = combined_df.reset_index(drop=True)
combined_df = combined_df.dropna()

print(combined_df.head())
print(combined_df.tail())

r1, c1 = (df1.shape)
print('\n', 'Number of ROWS & COLUMNS in Dataset 1:', r1, c1)

r2, c2 = (df2.shape)
print('\n', 'Number of ROWS & COLUMNS in Dataset 2:', r2, c2)

r, c = (combined_df.shape)
print('\n', 'Number of ROWS & COLUMNS in Dataset COMBINED:', r, c)

combined_df.to_csv('new_file_combined.csv', index = False)

print(combined_df.isnull().sum())
rows_with_null = combined_df[combined_df.isnull().any(axis=1)]
print(rows_with_null)

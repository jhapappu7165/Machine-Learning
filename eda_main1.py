### QTA: Why not able to delete '' value in line 4105?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", on_bad_lines='skip', na_values=['NaN', '', 'null', 'nul', 'None'], skipinitialspace=True) #<--ignore leading spaces 
df = df.dropna() #DROP NULL VALUES
print(df)

print('\n', "LINE-BY-LINE IDENTIFICATION OF NULL VALUES")
print(df.isnull())
print('\n', 'NUMBER OF NULL VALUES')
print(df.isnull().sum())
print('\n', 'NUMBER OF UNIQUE VALUES')
print(df.nunique())
print('\n', 'DATA TYPES OF COLUMNS')
print(df.dtypes)
print('\n', 'DESCRIBING THE DATASET')
print(df.describe())
print('\n', 'INFORMATION ABOUT DATASET')
print(df.info())

print('\n', 'ROWS WITH NULL VALUES')
rows_with_null = df[df.isnull().any(axis=1)]
print(rows_with_null)

print('\n', 'INDEX OF ROWS WITH NULL VALUES')
print(rows_with_null.index)

rows, cols = df.shape
print('\n', 'Number of rows: ', rows, '\n', 'Number of columns: ', cols)

print('\n', 'SORTING COLUMNS ==> PASSWORD & STRENGTH')
print(df.sort_values(by='password', ascending=True))
print(df.sort_values(by='strength', ascending=True))


#print('\n', 'TIME FOR VISUALIZATION')
#sns.heatmap(df.isnull())
#plt.title('HEATMAP')
#plt.show()


#******* DATA CLEANING *********************
df = df.drop_duplicates()
print('\n', 'DATAFRAME AFTER DROPPING DUPLICATES', df.head())

rws, colns = df.shape
print('\n', 'Number of rows & columns after dropping DUPLICATES: ', rws, colns)

#print(df.count()) #count of rows in each column

print('\n', 'GROUPING BASED ON PASSWORD STRENGTH')
print(df.groupby('strength').size())

### LINE GRAPH
#df.groupby('strength').size().plot()
#plt.show()


### BOX PLOT
#df.boxplot(column='strength')
#plt.show()


### REMOVE NON-ALPHABETIC CHARACTERS
df['password'] = df['password'].str.replace('[^A-Za-z0-9]', '', regex=True)

# Set display option to show all rows
pd.set_option('display.max_rows', None)
#print(df)


## WHY INDEXING IS NOT AS EXPECTED? ANSWER: Several data deleted (rows with 5 columns) & 1 row with Null value
print(df.iloc[586383])

df.to_csv('new_file1.csv', index=False)

#QTA: How to ensure that I choose the fifth column value as my password's strength and prevents the loss of five-column rows?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("passwords.csv", on_bad_lines='skip', na_values=['NaN', '', 'null', 'nul', 'None'])
df = df.dropna() #DROP NULL VALUES
df = df.drop(columns=['rank', 'category', 'value', 'time_unit', 'offline_crack_sec', 'rank_alt', 'font_size']) #drop unnecessary column


#****relabel strength coln by replacing 1-4 by 0, 5-8 by 1, and 9+ by 2****
#***cut() splits values into different ranges; 'bins' defines ranges for splitting the "strength" values; (-1,4],(4,8),(8,infinity), 'labels' to replace original values
df['strength'] = pd.cut(df['strength'], bins=[-1, 4, 8, float('inf')], labels=[0, 1, 2]) 


print('\n', "****LINE-BY-LINE IDENTIFICATION OF NULL VALUES****")
print(df.isnull())
print('\n', '****NUMBER OF NULL VALUES****')
print(df.isnull().sum())
print('\n', '****NUMBER OF UNIQUE VALUES****')
print(df.nunique())
print('\n', '****DATA TYPES OF COLUMNS****')
print(df.dtypes)
print('\n', '****DESCRIBING THE DATASET****')
print(df.describe())
print('\n', '****INFORMATION ABOUT DATASET****')
print(df.info())

print('\n', '****ROWS WITH NULL VALUES****')
rows_with_null = df[df.isnull().any(axis=1)]
print(rows_with_null)

print('\n', '****INDEX OF ROWS WITH NULL VALUES****')
print(rows_with_null.index)

rows, cols = df.shape
print('\n', 'Number of rows: ', rows, '\n', 'Number of columns: ', cols)


print('\n', '**********SORTING COLUMNS ==> PASSWORD & STRENGTH****************')
print('****SORTING BASED ON password column in ASCENDING order****')
print(df.sort_values(by='password', ascending=True))
print('\n', '****SORTING BASED ON strength column in ASCENDING order****')
print(df.sort_values(by='strength', ascending=True))


#print('\n', 'TIME FOR VISUALIZATION')
#sns.heatmap(df.isnull())
#plt.title('HEATMAP')
#plt.show()

print('\n', '***ROW 18 values***')
print(df.iloc[18])

#******* DATA CLEANING *********************
df = df.drop_duplicates()
print('\n', '****DATAFRAME AFTER DROPPING DUPLICATES****', '\n', df.head())

rws, colns = df.shape
print('\n', '****Number of rows & columns after dropping DUPLICATES: ', rws, colns)

#print(df.count()) #count of rows in each column


print('\n', '****GROUPING BASED ON PASSWORD STRENGTH****')
print(df.groupby('strength', observed=True).size())


### LINE GRAPH
#df.groupby('strength').size().plot()
#plt.show()


### BOX PLOT
#df.boxplot(column='strength')
#plt.show()


### REMOVE NON-ALPHABETIC CHARACTERS
df['password'] = df['password'].str.replace('[^A-Za-z0-9]', '', regex=True)


# Set display option to show all rows
pd.set_option('display.max_rows', 100)
print('\n', df)

df.to_csv('new_file2.csv', index=False)

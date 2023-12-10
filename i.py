import pandas as pd
import numpy as np
import datetime
data= pd.read_csv('C:\\Users\\eraia\\OneDrive\\Documents\\datasets\\sample.csv')
head=data.head(10)
#print(head)
columns = list(data.columns)
#print(columns)
'''print("Missing values distribution: ")
print(data.isnull().mean())

print(data.dtypes)'''

# examining rows with null values for date_added column
rows = []
for i in range(len(data)):
    if data['date_added'].iloc[i] == "":
        rows.append(i)
    
# examine those rows to confirm null state
data.loc[rows, :]
# extracting months added and years added
month_added = []
year_added = []
for i in range(len(data)):
    # replacing NaN values with 0
    if i in rows:
        month_added.append(0)
        year_added.append(0)
    else:
        date = data['date_added'].iloc[i].split(" ")
        month_added.append(date[0])
        year_added.append(int(date[2]))
        
# turning month names into month numbers
for i, month in enumerate(month_added):
    if month != 0:
        datetime_obj = datetime.strptime(month, "%B")
        month_number = datetime_obj.month
        month_added[i] = month_number
        
# checking all months
print(set(month_added))
print(set(year_added))

# inserting the month and year columns into the dataset
data.insert(7, "month_added", month_added, allow_duplicates = True)
data.insert(8, "year_added", year_added, allow_duplicates = True)
data.head()

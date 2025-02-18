import numpy as np
import pandas as pd

array_data = np.array([
    [101, "Alice", 25],
    [102, "Bob", 30],
    [103, "Charlie", 27]
])

df = pd.DataFrame(array_data, columns=["ID", "Name", "Age"])
print(df)

#selecting a column
print("printing name column:")
print(df["Name"])

# Selects multiple columns
print("printing name,Age column:")
print(df[["Name", "Age"]])  

#printing a row by index
print("printing row by index:")
print(df.iloc[0])

#selecting row where name=Alice
print("selecting row where name=Alice:")
print(df.loc[df["Name"] == "Alice"])

# Removes "Age" column
df = df.drop(columns=["Age"])  
print(df)

# Selects only rows where Age > 26
df_filtered = df[df["Age"] > 26]  
print("Selects only rows where Age > 26")
print(df_filtered)

#sorting data
df_sorted = df.sort_values(by="Age", ascending=False)
print(df_sorted)

#check missing data
print("check missing data")
print(df.isnull())

#drop missing data
print("drop missing data")
df.dropna()


#fill missing data with 0
print("fill missing data with 0")
df.fillna(0, inplace=True)
print(df)




import pandas as pd
data_dict = {
    "ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 27],
    "Department": ["HR", "IT", "Finance"]
}

df = pd.DataFrame(data_dict)
print(df)

import pandas as pd

data = [
    [101, "A", 25, "HR"],
    [102, "B", 30, "IT"],
    [103, "C", 27, "Finance"]
]

# Creating the DataFrame
df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Department"])

print(df)

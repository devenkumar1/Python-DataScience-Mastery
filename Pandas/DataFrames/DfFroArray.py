import numpy as np
import pandas as pd

array_data = np.array([
    [101, "Alice", 25],
    [102, "Bob", 30],
    [103, "Charlie", 27]
])

df = pd.DataFrame(array_data, columns=["ID", "Name", "Age"])
print(df)

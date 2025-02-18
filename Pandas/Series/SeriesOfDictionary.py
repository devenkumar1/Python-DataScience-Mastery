import pandas as pd

data_dict = {'a': 100, 'b': 200, 'c': 300}

#creating series from  a dictionary
series4 = pd.Series(data_dict)
print(series4)
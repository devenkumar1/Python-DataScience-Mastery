import pandas as pd

#list
data=[1,2,3,4,5]
index=["A","B","C","D","E"] 

#making Series from the list
series=pd.Series(data)
print("series:")
print(series)

series_with_custom_index=pd.Series(data, index=index)
print("series with custom index:")
print(series_with_custom_index)
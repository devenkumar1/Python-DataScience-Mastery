import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5]
series = pd.Series(data)

print(series)

#accesing via index
print("accesing via index: ") 
print(series[2]) 

print("slicing the series")
print(series[0:2]) 

#adding 10 to the series
print("addinf 10 to the series: ")
print(series + 10)

#mutiplying the series by 2
print("multiplying 2 to the series: ")
print(series * 2)

#check series is null or not
series7 = pd.Series([10, np.nan, 30, None])
print("checking if the series is null: ")
print(series7.isnull())



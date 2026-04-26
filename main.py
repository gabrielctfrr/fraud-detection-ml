import pandas as pd 

df = pd.DataFrame({'a':[1, None, 3], 'b':[4, 5, None]})
print(df.isnull().sum())
print(type(df.isnull().sum()))
print(df.isnull().sum().any())
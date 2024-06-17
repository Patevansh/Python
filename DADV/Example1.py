import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("E:\Python\Data.csv.xlsx")
print(data)
print(data.head())
print(data.tail())
print(data.shape)
print(data.info())
print(data.nunique())
print(data.isnull().sum())
x=data['X Values']
y=data['Y Values']
plt.bar(x,y,width=5)
plt.xlabel("x")
plt.ylabel("y")
plt.pie(data["Value"],labels=data["Label"])
plt.show()

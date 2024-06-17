import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("E:\Python\Car Inventory_DADV_2024.xlsx")
print(data)
print(data.head())
print(data.tail())
print(data.shape)
print(data.info())
print(data.nunique())
print(data.isnull().sum())
data=data.drop(['Make'],axis=1)
print(data.info())
print(data.max())
print(data.describe().T)
x=data['Model']
y=data['Cost']
plt.bar(x,y,width=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
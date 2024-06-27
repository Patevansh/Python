import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

file = pd.read_excel('E:\Python\Students.xlsx')
print(file)

mean_age=file['Age'].mean()
mean_customer=file['Customer'].mean()
median1=file['Age'].median()
median2=file['Customer'].median()
mode1=file['Age'].mode()
mode2=file['Customer'].mode()

print(mean_age,mean_customer,median1,median2,mode1,mode2)
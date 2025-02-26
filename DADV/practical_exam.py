
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file =pd.read_csv("homeprices.csv")
p=file.drop("price",axis=1)
q=file["price"]
p_train ,p_test,q_train,q_test=train_test_split(p,q,test_size=0.3,shuffle=True,random_state=40)
lr=LinearRegression()

lr.fit(p_train,q_train)

q_pre=lr.predict(p_train)
plt.plot(p_train,q_train,'bo')
plt.plot(p_train,q_pre,'r-')

q_pre=lr.predict(p_test)
plt.plot(p_test,q_test,'ro')
plt.plot(p_test,q_pre,'b-')

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset=datasets.load_iris()
x=dataset.data
y=dataset.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
accuracy=metrics.accuracy_score(y_test,y_pred)
confusion_matrics=metrics.confusion_matrix(y_test,y_pred)
print("Accuracy :" , accuracy)
print("Confusion matrix: ")
labels=dataset.target_names
sns.heatmap(confusion_matrics,annot=True,fmt="d",xticklabels=labels,cmap="Blues",cbar=False)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()
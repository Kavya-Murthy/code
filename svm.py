from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = load_breast_cancer()
x = data.data
y = data.target
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2)

clf = SVC(kernel='rbf', C=3)
clf.fit(X_train,Y_train)

print(clf.score(X_test,Y_test))

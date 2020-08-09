import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("C:\\Users\\Sanju Bosco\\Desktop\\python files\\Python projects\\Machine Learning\\car.data")
print(data.head())

bn = preprocessing.LabelEncoder()
buying = bn.fit_transform(list(data["buying"])) 
maint = bn.fit_transform(list(data["maint"])) 
door = bn.fit_transform(list(data["door"])) 
persons = bn.fit_transform(list(data["persons"])) 
lug_boot = bn.fit_transform(list(data["lug_boot"])) 
safety = bn.fit_transform(list(data["safety"]))  
cls = bn.fit_transform(list(data["class"])) 

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)
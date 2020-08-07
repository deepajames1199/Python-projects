import pandas as pd 
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

#read csv file to a variable "data"
data = pd.read_csv('C:\\Users\\Sanju Bosco\\Desktop\\python files\\Python projects\\Machine Learning\\student-mat.csv',sep=";")
#taking the required attributes to train and test
data = data[["G1",'G2','G3','studytime','failures','absences']]
#determine the label(that has to be predicted)
predict = "G3"
#separating the attributes and label into two arrays
X = np.array(data.drop([predict],1)) 
y = np.array(data[predict])
#splitting up the train and test datas 
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
#Looping to iterate to a certain value to find the best accuracy
#Inside loop: Training the model in a linear aggression algorithm using the train datas
#             Finding the accuracy of the algorithm by using the test datas
#             Writing the model corresponding to the best accuracy to a pickle file
'''
best = 0
for a in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f: 
            pickle.dump(linear, f)
'''
#reading the pickle file and loading it to the linear model 
best_data = open("studentmodel.pickle", "rb")
linear = pickle.load(best_data)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

#predicting the output from the trained model by giving the test data(x_test) as argument
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])  

#plotting the graph for output grade versus any one of the attributes to find the datapoints and correlation between the two axis
p = 'G1'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show() 
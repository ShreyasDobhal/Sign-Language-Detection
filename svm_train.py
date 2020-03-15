import scipy.misc as misc
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import sklearn
from sklearn.metrics import classification_report
import pickle
import csv
from random import shuffle

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-2,5e-3,1e-1,5e-2],'C': [1, 5, 10, 100, .1], 'probability': [True]}]
scores = ['accuracy']
test_train_split_ratio = 0.7
lookup = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
# sorted(sklearn.metrics.SCORERS.keys())

X_data = []
Y_data = []
dataSet = []
with open('Data/dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # rowCnt = 0
    for row in csv_reader:
        if row[0] in lookup:
            values = [lookup[row[0]],row[1],row[2],row[3],row[4]]
            dataSet.append(values)
            # rowCnt += 1
            # if rowCnt == 16:
            #     break

# dataSet = dataSet[1:]
shuffle(dataSet)
print (dataSet)
for values in dataSet:
    X_data.append(values[1:])
    Y_data.append(values[0])

X_train = X_data[0:(int)(len(X_data)*test_train_split_ratio)]
X_test = X_data[(int)(len(X_data)*test_train_split_ratio):]
Y_train = Y_data[0:(int)(len(Y_data)*test_train_split_ratio)]
Y_test = Y_data[(int)(len(Y_data)*test_train_split_ratio):]

X_train = np.asarray(X_train)
X_test = np.asarray(X_test)
Y_train = np.asarray(Y_train)
Y_test = np.asarray(Y_test)

print (X_train.shape)
print (Y_train.shape)
print (Y_train)
for score in scores:
    clf = GridSearchCV(SVC(), tuned_parameters, cv=5, scoring='%s' % score)

    clf.fit(X_train, Y_train)
    #print()
    svc_estimator = clf.best_estimator_
    #y_true, y_pred_prob = y_test, svc_estimator.predict_proba(X_test)
    Y_pred = svc_estimator.predict(X_test)

count = 0
for i in  range (len(Y_pred)):
    if Y_pred[i]==Y_test[i]:
        count +=1
acc = count / len(Y_test)
print ("Accuracy : " + str(acc))

pickle.dump(svc_estimator, open('classification.sav', 'wb'))

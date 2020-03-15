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

import serial
from serial import Serial
from time import sleep
from values import ARDUINO_PORT, BAUD_RATE
import csv

lookup = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

arduino = Serial(ARDUINO_PORT, BAUD_RATE, timeout = 0.1)

print ("Loading model")
loaded_model = pickle.load(open('classification.sav', 'rb'))
print ("Model loaded")

def getBytes(msg):
    return bytes(msg,'utf-8')

print ("Starting . . . ")
sleep(1)
arduino.write(getBytes("5"))
sleep(1)
while True:
    try:
        data = arduino.readline()[:-2]
        if data:
            data = str(data)
            data = data[2:-1]
            values = data.split(',')
            rowData = []
            for value in values:
                tmp = value[value.find(': ')+2:]
                rowData.append(tmp)
            features = rowData[1:]
            features = np.asarray(features,dtype='float32')
            # print (features)
            features = np.reshape(features,(1,4))
            prediction = loaded_model.predict(features)
            print ("Output : " + lookup[prediction[0]])
    except:
        continue
arduino.write(getBytes("5"))    
sleep(5)
print ("Completed")


    
    

# b'x: 317.86, y: 31.36, z: 303.97, f: 442'

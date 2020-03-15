import serial
from serial import Serial
from time import sleep
from values import ARDUINO_PORT, BAUD_RATE
import csv


arduino = Serial(ARDUINO_PORT, BAUD_RATE, timeout = 0.1)
fileName = 'dataset.csv'

labels = ['A','B','C','G','P','Q']
readingCnt = 2000

def getBytes(msg):
    return bytes(msg,'utf-8')

for label in labels:
    print ("Detecting " + label)
    sleep(10)
    arduino.write(getBytes("5"))
    sleep(1)
    for i in range (readingCnt):
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
                rowData[0] = label
                print (rowData)
                with open(fileName, 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(rowData)
                csvFile.close()
        except:
            continue
    arduino.write(getBytes("5"))
    sleep(1)
    print (label + " done")
print ("Done")


    
    

# b'x: 317.86, y: 31.36, z: 303.97, f: 442'

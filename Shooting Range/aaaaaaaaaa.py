'''
Guter Gott
Maximilian
9.12.2022
'''

import serial


ser = serial.Serial('COM3', 9600)

ser = serial.Serial('COM3', 9600)
ser.write('1')
ser.close()
data = ser.read()

print(data)

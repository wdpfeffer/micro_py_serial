import serial
ser = serial.Serial('com4',9600)
ser.flushInput()

while True:
    sin=ser.readline()
    if sin:
        print(sin.decode('utf-8'))
    

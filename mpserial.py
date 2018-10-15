import serial
ser = serial.Serial('com4', 9600, timeout = 1)
ser.flushInput()

# while True:
#     sin=ser.readline()
#     if sin:
#         print(sin.decode('utf-8'))
    

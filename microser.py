from machine import UART

uart = UART(1, 9600)
uart.init(9600, bits = 8, parity = None, stop = 1)

while True:
    rs = uart.readline()
    if rs:
        print(rs.decode('utf-8'))
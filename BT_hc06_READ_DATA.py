from machine import UART
import time
import utime
import ustruct as struct

uart = UART(2, 9600)
uart.init(9600, bits=8, parity=None, stop=1)
print(uart)

while True:
    if uart.any():
        while uart.any():
            buf = uart.read()
            lst = struct.unpack('iiii', buf)
            print('received:',lst[0],lst[1],lst[2],lst[3])
            utime.sleep_ms(15)

        utime.sleep_ms(10)
        try:
            uart.write(struct.pack('ii', lst[0],lst[1]))
            print('sent response')
        except OSError:
            pass
        
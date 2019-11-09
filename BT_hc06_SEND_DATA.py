from machine import UART
import time
import utime
import ustruct as struct

uart = UART(2, 9600)
uart.init(9600, bits=8, parity=None, stop=1)
print(uart)

num_successes = 0
num_failures = 0

while num_successes < 10:
    lst =[utime.ticks_ms(),17,18,19]
    print('Sending:', lst)
    try:
        uart.write(struct.pack('iiii', lst[0],lst[1],lst[2],lst[3]))        
    except OSError:
        pass
    
    # wait for response    
    start_time = utime.ticks_ms()
    timeout = False
    while not uart.any() and not timeout:
        if utime.ticks_diff(utime.ticks_ms(), start_time) > 250:
            timeout = True

    if timeout:
        print('Failed, response timed out')
        num_failures += 1

    else:
        rlst = struct.unpack('ii', uart.read())
        print('Got data:', rlst[1] ,'in', utime.ticks_diff(utime.ticks_ms(), rlst[0]), 'ms')
        num_successes += 1

    utime.sleep_ms(250)

print('finished sending: successes=%d, failures=%d' % (num_successes, num_failures))

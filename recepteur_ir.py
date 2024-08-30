# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

import time
from machine import Pin
from ir_rx import NEC_16

led = Pin(2, Pin.OUT)

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        print('Data {:02x} Addr {:04x}'.format(data, addr))
    if data == 0x0d:
        led.on()
    if data == 0x1f:
        led.off()
        
ir = NEC_16(Pin(14, Pin.IN), callback)
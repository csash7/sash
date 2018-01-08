from gpiozero import LED
from gpiozero.pins.pigpiod import PiGPIOPin
from time import sleep

pin_a = PiGPIOPin(21, host='192.168.0.103')  # reference to pin 2 on a different Pi
#pin_b = PiGPIOPin(2, host='192.168.1.3')  # reference to pin 2 on another Pi

red = LED(pin_a)  # led on different Pi

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

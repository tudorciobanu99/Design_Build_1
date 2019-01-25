import machine
import time
green = machine.Pin(33, machine.Pin.OUT)
red = machine.Pin(27, machine.Pin.OUT)
flashlight = machine.PWM(machine.Pin(12))
def blink(led1, led2, flashlight):
    counter = 0
    active = True
    flashlight.value(1)
    while(active):
        if (counter < 5):
            counter += 1
            led1.value(1)
            time.sleep(0.5)
            led1.value(0)
            time.sleep(0.5)
        else:
            flashlight.value(0)
            led2.value(1)
            active = False
            time.sleep(5)
    led2.value(0)
blink(green, red, flashlight)

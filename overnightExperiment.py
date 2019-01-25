import time
import machine
import math
duty = 10
led = machine.PWM(machine.Pin(12))
sensor = machine.ADC(machine.Pin(33))
pin = machine.Pin(27, machine.Pin.OUT)
pin.value(1)
sensor.ATTN_11DB
green = machine.Pin(15, machine.Pin.OUT)
red = machine.Pin(32, machine.Pin.OUT)
led.freq(78000)
led.duty(duty)
button = machine.Pin(14, machine.Pin.IN)
inUse = False
isPressed = False
iterations = 0
intensity0 = 100.0

#beggining
green.value(1)
time.sleep(0.1)
green.value(0)
red.value(1)
time.sleep(0.1)
red.value(0)
green.value(1)
time.sleep(0.1)
green.value(0)
red.value(1)
time.sleep(1)
red.value(0)
#stop

active = True

while (active):
    if (isPressed == False and button.value() == 0):
        isPressed = True
    if (button.value() == 1 and isPressed == True and inUse == False):
        f = open("data.txt", "w")
        green.value(1)
        inUse = True
        while (inUse == True):
            data = []
            for i in range(5):
                data.append(sensor.read())
            average = sum(data) / 5
            iterations += 1
            f.write(str(iterations) + "," + str(average) + "\n")
            time.sleep(3)
            if (button.value() == 0):
                f.close()
                inUse = False
                green.value(0)
                red.value(1)
                f = open("data.txt", "r")
                g = open("OD.txt", "w")
                for line in f:
                    temp = line.split(",")
                    od = - math.log((float(temp[1])/intensity0),10)
                    g.write(str(temp[0]) + "," + str(od) + "\n")
                f.close()
                g.close()
                active = False
                red.value(0)
            time.sleep(60)

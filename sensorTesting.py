import machine
import time
changeInLED = 10
currentDuty = 0
led = machine.PWM(machine.Pin(12))
sensor = machine.ADC(machine.Pin(33))
pin = machine.Pin(27, machine.Pin.OUT)
pin.value(1)
sensor.ATTN_11DB
green = machine.Pin(15, machine.Pin.OUT)
red = machine.Pin(32, machine.Pin.OUT)
led.freq(78000)
led.duty(currentDuty)
f = open("data.txt", "w")
data = []
for i in range(103):
    green.value(1)
    for j in range(10):
        value = sensor.read()
        data.append(value)
        time.sleep(0.1)
    average = sum(data) / 10
    print(average)
    f.write(str(average) + "-----" + str(currentDuty) + "; ")
    data = []
    currentDuty += changeInLED
    led.duty(currentDuty)
green.value(0)
red.value(1)
f.close()
time.sleep(2)
red.value(0)

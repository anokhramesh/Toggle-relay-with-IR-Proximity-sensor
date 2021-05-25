# In this Project we will Interface a IRProximity sensor with Raspberry pi pico to toggle a
# Relay
from machine import Pin
import time
IR_proximity= machine.Pin(16,Pin.IN,Pin.PULL_DOWN)#connected the IR sensor Output to GPIO Pin 16
Relay = Pin(17,Pin.OUT)
while True:
    if IR_proximity.value()==1:#if IR Sensor outPut Is High
        Relay.toggle()#change the Relay status OFF to ON/ON to OFF
        time.sleep(0.5)
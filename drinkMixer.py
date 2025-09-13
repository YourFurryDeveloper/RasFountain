import rpi.gpio as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)

def mix(drinkName):
    if drinkName == "Water":
        gpio.output(23, gpio.HIGH)
        time.sleep(1)
        gpio.output(23, gpio.LOW)
        
        gpio.cleanup()
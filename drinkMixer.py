import pigpio
import time

pi = pigpio.pi()
pi.set_mode(23, pigpio.OUTPUT)

def mix(drinkName):
    if drinkName == "Water":
        pi.write(23, 1)
        time.sleep(1)
        pi.write(23, 0)
        
def stopPumpD():
    pi.stop()
    print("Pigpio daemon stopped")
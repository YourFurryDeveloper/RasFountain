import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

def openValve():
    pi.set_servo_pulsewidth(12, 500)
    
def closeValve():
    pi.set_servo_pulsewidth(12, 1300)

def mix(drinkName):
    if drinkName == "Water":
        openValve()
        time.sleep(1)
        closeValve()
        
def stopPumpD():
    pi.stop()
    print("Pigpio daemon stopped")
    quit()
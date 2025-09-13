import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

def openValve():
    pi.hardware_PWM(12, 50, 3000)  # Move servo
    time.sleep(0.5)                # Let it reach the position
    pi.hardware_PWM(12, 0, 0)      # Stop PWM to prevent shudder

def closeValve():
    pi.hardware_PWM(12, 50, 30589)
    time.sleep(0.5)
    pi.hardware_PWM(12, 0, 0)

def init():
    pi.set_PWM_frequency(12, 50)
    closeValve()

def mix(drinkName):
    if drinkName == "Water":
        openValve()
        time.sleep(1)
        closeValve()

def stopPumpD():
    pi.stop()
    print("Pigpio daemon stopped")
    quit()

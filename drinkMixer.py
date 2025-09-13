import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

def openValve():
    angle = 0
    pulse_width = 1000000 + (angle / 180) * 1000000
    pi.hardware_PWM(12, 50, pulse_width)  # Move servo
    time.sleep(0.5)                # Let it reach the position
    pi.hardware_PWM(12, 0, 0)      # Stop PWM to prevent shudder

def closeValve():
    angle = 20
    pulse_width = 1000000 + (angle / 180) * 1000000
    pi.hardware_PWM(12, 50, pulse_width)
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

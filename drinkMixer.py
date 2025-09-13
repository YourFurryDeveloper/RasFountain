import pigpio
import time

pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

def angle_to_dutycycle(angle):
    min_dc = 50000   # 1.0 ms pulse width
    max_dc = 100000  # 2.0 ms pulse width
    return int(min_dc + (angle / 180.0) * (max_dc - min_dc))

def openValve():
    pi.hardware_PWM(12, 50, angle_to_dutycycle(0))
    pi.hardware_PWM(12, 0, angle_to_dutycycle(0))

def closeValve():
    pi.hardware_PWM(12, 50, angle_to_dutycycle(20))
    pi.hardware_PWM(12, 0, angle_to_dutycycle(0))

def init():
    pi.set_PWM_frequency(12, 50)
    closeValve()

def mix(drinkName):
    if drinkName == "Water":
        openValve()
        time.sleep(3)
        closeValve()

def stopPumpD():
    pi.stop()
    print("Pigpio daemon stopped")
    quit()

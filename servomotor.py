import pigpio
import time

servoPIN = 12



def init():
    global pi 
    pi = pigpio.pi()
    pi.hardware_PWM(servoPIN , 50, 5*10000 )

def changeDutyCycle(dutyCycle):
    global pi  
    pi.hardware_PWM(servoPIN , 50, dutyCycle * 10000 )


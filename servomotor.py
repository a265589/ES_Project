import RPi.GPIO as GPIO
import time

servoPIN = 12



def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    global p 
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz  
    p.start(10) # the gate is close

def changeDutyCycle(dutyCycle):
    global p 
    p.ChangeDutyCycle(dutyCycle)


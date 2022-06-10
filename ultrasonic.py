import RPi.GPIO as GPIO 
import time 

GPIO_ECHO = 17
GPIO_TRIG = 27

SOUNDSPEED = 34000 # cm/s

distance = 10000

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_ECHO, GPIO.IN) 
    GPIO.setup(GPIO_TRIG, GPIO.OUT)

def getDistance():
    time.sleep(0.6)
    GPIO.output(GPIO_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, False)
    StartTime = time.time()
    StopTime = time.time()
     
        # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
     
        #save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
     
        # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
    distance = (TimeElapsed * SOUNDSPEED) / 2
    return  distance
    

if __name__ == '__main__':
    init()
    while True:
       
        print(getDistance())
    


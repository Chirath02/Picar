import RPi.GPIO as GPIO
import time
from gpioPinSettings import *


class Ultrasonic(object):
    def __init__(self):
        print("setting up pins")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(FRONT_TRIGGER, GPIO.OUT)         #initialising port as output
        GPIO.setup(RIGHT_TRIGGER, GPIO.OUT)         #initialising port as output
        GPIO.setup(BACK_TRIGGER, GPIO.OUT)          #initialising port as output
        GPIO.setup(LEFT_TRIGGER, GPIO.OUT)          #initialising port as output
        GPIO.setup(ECHO_PIN, GPIO.IN)               #initialising port as input

        GPIO.output(FRONT_TRIGGER, False)           #initialising port value as False
        GPIO.output(RIGHT_TRIGGER, False)           #initialising port value as False
        GPIO.output(BACK_TRIGGER, False)            #initialising port value as False
        GPIO.output(LEFT_TRIGGER, False)            #initialising port value as False

        print("Waiting For Sensor To Settle")
        time.sleep(1)

    def measure(self,TRIG,ECHO_PIN):                #measuering the distance
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO_PIN)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO_PIN)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)
        return distance

    def distance(self):                                #calling 4 Sensors and returning distance
        front = self.measure(FRONT_TRIGGER, ECHO_PIN)
        time.sleep(0.025)
        right = self.measure(RIGHT_TRIGGER, ECHO_PIN)
        time.sleep(0.025)
        back = self.measure(BACK_TRIGGER, ECHO_PIN)
        time.sleep(0.025)
        left = self.measure(LEFT_TRIGGER, ECHO_PIN)
        time.sleep(0.025)
        print([front, right, back, left])
        return [front, right, back, left]

    def close(self):                        #exit
        GPIO.setup(ECHO_PIN,GPIO.IN)
        GPIO.cleanup()

var = Ultrasonic()
print var.distance()

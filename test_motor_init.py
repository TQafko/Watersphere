import RPi.GPIO as GPIO
from motor import Motor
import time

# Testing two reaction wheels
m1 = Motor(6,19,12,1000,0)
m2 = Motor(5,0,13,1000,0)

m1.test_motor()
m2.test_motor()

m1.shutdown() # only once as it calls gpio cleanup on all gpio

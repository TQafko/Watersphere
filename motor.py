# Tedi Qafko Date:7/7/2024
# Description: Control L298N motor driver 
import RPi.GPIO as GPIO
import time

class Motor:
    '''
    IN pins - Control rotation direction of motors
    EN pin -  Expects pwm to control speed or 0 or 1 for off or full speed
    Setup m1: in1 = 6, in2 = 19, en1 = 12
    Setup m2: in3 = 5, in5 = 0, en2 = 13
    '''
    def __init__(self,
                 in1 = 6,
                 in2 = 19,
                 en1 = 12,
                 pwm = 1000,
                 init_m1 = 0): # this is duty cycle of pwm
        
        self.in1 = in1
        self.in2 = in2
        self.en1 = en1
        self.pwm = pwm
        self.init_m1 = init_m1
        print("Initilizing GPIO for motors...\n")
        GPIO.setmode(GPIO.BCM) # Defines pi pins as diagrams
        GPIO.setup(in1, GPIO.OUT) # Setting all pins to output
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en1, GPIO.OUT)
        # (IN) pins are two bit logic for clockwise, counter-clockwise
        # and stopping a motor
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        # (EN) pins enable changing the speed of the motor via 
        # pulse width modulated (PWM) signals
        self.p1 = GPIO.PWM(en1, pwm)
        # Initially the motors will be set to 0.
        self.p1.start(init_m1)
        print("Motors initated Successfully!\n")

    def stop(self):
        print("Stop")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

    def forward(self):
        print("Forward")
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def backward(self):
        print("Backward")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def speed(self, cycle=25):
        ''' Duty Cycle is between 0-100 with 100 being the fastest'''
        print(f"Changing speed: ", cycle)
        self.p1.ChangeDutyCycle(cycle)

    def shutdown(self):
        '''This cleans up all GPIO, only run if needed'''
        GPIO.cleanup()

    def test_motor(self):
        '''Runs motor for 2 seconds at 25 duty cycle'''
        print("Start Test\n")
        self.forward()
        self.speed(25)
        time.sleep(2)
        self.backward()
        time.sleep(2)
        self.stop()
        self.speed(0)
        print("Stop Test\n")
        time.sleep(2)
        print("Success!\n")

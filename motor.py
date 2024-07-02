import RPi.GPIO as GPIO
from time import sleep

in1 = 6
in2 = 19
in4 = 0
in3 = 5

en1 = 12
en2 = 13
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p1 = GPIO.PWM(en1, 1000)
p2 = GPIO.PWM(en2, 1000)
p1.start(25)
p2.start(0)

print("\n")
print("r-run, s-stop, f-forward, b-backward, l-low, m-medium, h-high, e-exit")
print("\n")

while(1):
    x = input()
    if x == 'r':
        print("run")
        if(temp1 == 1):
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("backward")
            x = 'z'
    elif x == 's':
        print("stop")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
    elif x == 'f':
        print("forward")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        temp1 = 1
        x = 'z'
    elif x == 'b':
        print("backward")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        temp1 = 0
        x = 'z'
    elif x == 'l':
        print("low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        x = 'z'
    elif x == 'm':
        print("medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x = 'z'
    elif x == 'h':
        print("high")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
    elif x == 'e':
        GPIO.cleanup()
        break
    else:
        print("Wrong Data")

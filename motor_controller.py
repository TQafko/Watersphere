import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1 = 17  # Motor A direction control
IN2 = 27  # Motor A direction control
IN3 = 22  # Motor B direction control
IN4 = 23  # Motor B direction control

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

pwm_1 = GPIO.PWM(IN1, 100)  # 100 Hz frequency
pwm_2 = GPIO.PWM(IN2, 100)  # 100 Hz frequency
pwm_3 = GPIO.PWM(IN3, 100)  # 100 Hz frequency
pwm_4 = GPIO.PWM(IN4, 100)  # 100 Hz frequency

motor1 = (pwm_1, pwm_2)
motor2 = (pwm_3, pwm_4)

def motor_init(motors):
	for motor in motors:
		motor.start(0)
	return 0

# 1 == Forward ; 0 == Backward
# Speed 0-100
def set_motor_speed(motor, speed, direction):
	if direction == 1: 
		motor[0].ChangeDutyCycle(speed)
		motor[1].ChangeDutyCycle(0)
	else:
		motor[0].ChangeDutyCycle(0)
		motor[1].ChangeDutyCycle(speed)
	return 0

def test():
	motor_init(motor1)
	motor_init(motor2)
	runtime = float(input("How Long should this run for: "))
	starttime = time.time()
	elapsed = 0
	while elapsed < runtime:
		elapsed = time.time() - starttime
		print(elapsed)
		count = 0
		while count < 100:
			set_motor_speed(motor1, count, 1)
			set_motor_speed(motor2, 100 - count, 0)
			count += 1
	time.sleep(1)
	pwm_1.stop()
	pwm_2.stop()
	pwm_3.stop()
	pwm_4.stop()
	GPIO.cleanup()
	return 0

test()

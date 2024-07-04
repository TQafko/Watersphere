import board
import busio
import RPi.GPIO as GPIO
import time
from bno008 import bno008


i2c = busio.I2C(board.SCL, board.SDA)
imu = bno008(i2c)

while(1):
    x,y,z = imu.get_orientation()
    time.sleep(2)
    print (x)
    print (y)
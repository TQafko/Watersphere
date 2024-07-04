import time
import board
import math
import busio
import adafruit_bno08x
from adafruit_bno08x.i2c import BNO08X_I2C

def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)
    
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)
    
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
    
    return roll_x, pitch_y, yaw_z # in radians


i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
bno = BNO08X_I2C(i2c)
bno.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)
bno.enable_feature(adafruit_bno08x.BNO_REPORT_ACCELEROMETER)
bno.enable_feature(adafruit_bno08x.BNO_REPORT_GYROSCOPE)
bno.enable_feature(adafruit_bno08x.BNO_REPORT_MAGNETOMETER)
bno.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)



def bno_get_quat():
    # mag_x, mag_y, mag_z = bno.magnetic
    # gyro_x, gyro_y, gyro_z = bno.gyro
    # accel_x, accel_y, accel_z = bno.acceleration
    try:
        quat_i, quat_j, quat_k, quat_real = bno.quaternion
    except Exception as e:
        print("Error runtime")
        return
    roll_x, pitch_y, yaw_z = euler_from_quaternion(quat_i, quat_j, quat_k, quat_real)
    roll_x = math.degrees(roll_x)
    pitch_y = math.degrees(pitch_y)
    yaw_z = math.degrees(yaw_z)
    # print("I: %0.6f  J: %0.6f K: %0.6f  Real: %0.6f" % (quat_i, quat_j, quat_k, quat_real))
    print("Roll: %0.2f  Pitch: %0.2f Yaw: %0.2f" % (roll_x, pitch_y, yaw_z))


while(1):
    bno_get_quat()
    print("Waiting...\n")
    time.sleep(1)
# Date 7/3/2024
# Tedi Qafko
# Class object for inertial measurement unit device BNO085 for 
# receiving data of orientation

#define BNO08x_I2CADDR_DEFAULT 0x4A 
class bno008:
    import board
    from busio import I2C
    def __init__(self,i2c_bus,freq=400000):
        import adafruit_bno08x
        from adafruit_bno08x.i2c import BNO08X_I2C
        from adafruit_bus_device.i2c_device import I2CDevice
        self.freq = freq
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        try:
            self.bno = BNO08X_I2C(i2c_bus)
            self.bno.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)
            self.bno.enable_feature(adafruit_bno08x.BNO_REPORT_ACCELEROMETER)
            self.bno.enable_feature(adafruit_bno08x.BNO_REPORT_GYROSCOPE)
            self.bno.enable_feature(adafruit_bno08x.BNO_REPORT_MAGNETOMETER)
            self.bno.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR)
        except Exception as e:
            print(e)
            print("Failed to initialize....")
       
    def euler_from_quaternion(self, x, y, z, w):
        import math
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
    
    def get_orientation(self):
        import math
        # mag_x, mag_y, mag_z = bno.magnetic
        # gyro_x, gyro_y, gyro_z = bno.gyro
        # accel_x, accel_y, accel_z = bno.acceleration
        try:
            quat_i, quat_j, quat_k, quat_real = self.bno.quaternion
        except Exception as e:
            print(e)
            print("Failed to get data...")
            return -1, -1, -1 
        roll_x, pitch_y, yaw_z = self.euler_from_quaternion(quat_i, quat_j, quat_k, quat_real)
        self.roll = math.degrees(roll_x)
        self.pitch= math.degrees(pitch_y)
        self.yaw = math.degrees(yaw_z)
        # print("Roll: %0.2f  Pitch: %0.2f Yaw: %0.2f" % (roll_x, pitch_y, yaw_z))
        return self.roll, self.pitch, self.yaw # in degrees

# Example of how to use 
# import time    
# imu = bno008()
# while(1):
#     x, y, z = imu.get_orientation()
#     print("Roll is")
#     print(x)
#     time.sleep(2)

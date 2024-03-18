import time
import datetime
import board
import busio
import adafruit_ads1x15 as ADS
from adafruit_ads1x15 import AnalogIn

#Channel
def get_channel_value(channel, ads):
    channel = -1
    if channel == 0:
        channel = AnalogIn(ads, ADS.P0)
    elif channel == 1:
        channel = AnalogIn(ads, ADS.P1)
    elif channel == 2:
        channel = AnalogIn(ads, ADS.P2)
    elif channel == 3:
        channel = AnalogIn(ads. ADS.P3)
    return channel

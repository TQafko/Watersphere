import time
import datetime
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

channel0 = AnalogIn(ads, ADS.P0)
channel1 = AnalogIn(ads, ADS.P1)
channel2 = AnalogIn(ads, ADS.P2)
channel3 = AnalogIn(ads, ADS.P3)

adc_channels = [channel0, channel1, channel2, channel3]
adc_channel_voltage = [0, 0, 0, 0]
adc_channel_value = [0, 0, 0, 0]

dt = datetime.datetime.now()

def ack_channel_values(adc_channels, vals, voltages, elapsed_t, f):
		for channels in range(len(adc_channels)):
			vals[channels] = adc_channels[channels].value
			voltages[channels] = adc_channels[channels].voltage
			print("ADC {} Value: {}  Voltage {} \n".format(channels, vals[channels], voltages[channels]))
			f.write("{}   {}   {}\n".format(channels, voltages[channels], elapsed_t))	
		return 0

def record_function(adc_channels, adc_channel_value, adc_channel_voltage):
	time_in_seconds = float(input("How Long would you like to record for: "))
	start_t = time.time()
	elapsed_t = 0
	with open("{}.txt".format(dt), 'a+') as f:
		f.write("ADC CHANNEL   VOLTAGE   TIME\n")
		while(elapsed_t < time_in_seconds):
			ack_channel_values(adc_channels, adc_channel_value, adc_channel_voltage, elapsed_t, f	)
			elapsed_t = time.time() - start_t
	return 0


record_function(adc_channels, adc_channel_voltage, adc_channel_value)


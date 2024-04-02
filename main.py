from flask import Flask, render_template, jsonify, Response, request
import random
import datetime
import board
import busio
import numpy as np
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import picamera
import io
import RPi.GPIO as GPIO
import time
from motor_controller import *

app = Flask(__name__)

# I2C Variables
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
except:
    print("Error Initializing I2C Bus")
    exit()

channel0 = AnalogIn(ads, ADS.P0)
channel1 = AnalogIn(ads, ADS.P1)
channel2 = AnalogIn(ads, ADS.P2)
channel3 = AnalogIn(ads, ADS.P3)
adc_channels = [channel0, channel1, channel2, channel3]
adc_voltages = np.zeros((4, 100))

# Time Variables
dt = datetime.datetime.now()

# Function to read ADC channels and return an array of voltages: [C0, C1, C2, C3]
def read_channels(adc_channels):
    temp_arr = [0, 0, 0, 0]
    for idx, channel in enumerate(adc_channels):
        temp_arr[idx] = channel.voltage
    return temp_arr

def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        stream = io.BytesIO()

        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n'
            stream.seek(0)
            stream.truncate()

@app.route('/Hello')
def hello():
    # if 'Hello' in request.form:
    print("Hello")
    set_motor_speed(motor1, 50, 1)
    time.sleep(1)
    # elif 'Hello_else' in request.form:
    #     print("Hello_else")
    #     set_motor_speed(motor2, 50, 1)
    #     time.sleep(1)
    # else:
    stop_motor(motor1)
    stop_motor(motor2)
    return render_template('index.html')

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/update_data')
def update_data():
    voltages = read_channels(adc_channels)
    return jsonify(voltages=voltages)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", threaded=True)

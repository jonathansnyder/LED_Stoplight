import RPi.GPIO as GPIO
import threading
import time
from flask import Flask, render_template, request


stoplightctr = Flask(__name__)

#imports rpi library and grabs neccessary parts from flask

#using the board numbers for pins not broadcom
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Name the pin numbers
GreenLed = 11
YellowLed = 13
RedLed = 15

stop_thread = False
#set the stoplight pins to output
#pin green
GPIO.setup(GreenLed, GPIO.OUT)

#pin yellow
GPIO.setup(YellowLed, GPIO.OUT)

#pin red
GPIO.setup(RedLed, GPIO.OUT)

#initialize all lights off
GPIO.output(GreenLed, GPIO.LOW)
GPIO.output(YellowLed, GPIO.LOW)
GPIO.output(RedLed, GPIO.LOW)


@stoplightctr.route('/')
def index():
    return render_template('index.html')

@stoplightctr.route("/<option>")
def action(option):
    if option == 'Red':
        #only red light on
        stop_thread = True
        GPIO.output(RedLed, GPIO.HIGH)
        GPIO.output(YellowLed, GPIO.LOW)
        GPIO.output(GreenLed, GPIO.LOW)
    if option == 'Yellow':
        #only yellow light on
        stop_thread = True
        GPIO.output(RedLed, GPIO.LOW)
        GPIO.output(YellowLed, GPIO.HIGH)
        GPIO.output(GreenLed, GPIO.LOW)
    if option == 'Green':
        #only green light on
        stop_thread = True
        GPIO.output(RedLed, GPIO.LOW)
        GPIO.output(YellowLed, GPIO.LOW)
        GPIO.output(GreenLed, GPIO.HIGH)
    if option == 'none':
        #all lights off
        stop_thread = True
        GPIO.output(RedLed, GPIO.LOW)
        GPIO.output(YellowLed, GPIO.LOW)
        GPIO.output(GreenLed, GPIO.LOW)
    if option == 'auto':
        #run function
        stop_thread = False
        def autostoplight():
            while True:
                if stop_thread:
                    break
                #Turn on red
                GPIO.output(RedLed, GPIO.HIGH)
                #Wait 10 Seconds
                time.sleep(5)
                if stop_thread:
                    break
                    
                #Turn off Red, turn on Green
                GPIO.output(RedLed, GPIO.LOW)
                GPIO.output(GreenLed, GPIO.HIGH)
                #Wait 10 Seconds
                time.sleep(5)
                if stop_thread:
                    break
                    
                #Turn off Green, Turn on Yellow
                GPIO.output(GreenLed, GPIO.LOW)
                GPIO.output(YellowLed, GPIO.HIGH)
                #Wait 5 Seconds
                time.sleep(2)
                if stop_thread:
                    break
                #Turn off yellow
                GPIO.output(YellowLed, GPIO.LOW)
        threadone = threading.Thread(target = autostoplight)
        threadone.start()
        threadone.join()
    return render_template('index.html')


if __name__ == "__main__":
    stoplightctr.run(debug=True, port=80, host='0.0.0.0')

import RPI.GPIO as GPIO
from flask import Flask, render_template


stoplightctr = Flask(__name__)

#imports rpi library and grabs neccessary parts from flask

#using the board numbers for pins not broadcom
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Name the pin numbers
GreenLed = 11
YellowLed = 13
RedLed = 15

#set the stoplight pins to output
#pin green
GPIO.output(GreenLed, GPIO.OUT)

#pin yellow
GPIO.output(YellowLed, GPIO.OUT)

#pin red
GPIO.output(RedLed, GPIO.OUT)

#initialize all lights off
GPIO.output(GreenLed, GPIO.LOW)
GPIO.output(YellowLed, GPIO.LOW)
GPIO.output(RedLed, GPIO.LOW)


@stoplightctr.route('/index')
def index():
    return render_template('index.html')

@stoplightctr.route("/<option>")
def action(option):
    if option == Red:
        #only red light on
        GPIO.output(RedLed, GPIO.HIGH)
        GPIO.output(YellowLed, GPIO.LOW)
        GPIO.output(GreenLed, GPIO.LOW)
    if option == Yellow:
        #only yellow light on
        GPIO.output(RedLed, GPIO.LOW)
        GPIO.output(YellowLed, GPIO.HIGH)
        GPIO.output(GreenLed, GPIO.LOW)
    if option == Green:
        #only green light on
        GPIO.output(RedLed, GPIO.LOW)
        GPIO.output(YellowLed, GPIO.LOW)
        GPIO.output(GreenLed, GPIO.HIGH)
    if option == none:
        #all lights off
        GPIO.output(RedLed, GPIO.LOW)
        GPIO.output(YellowLed, GPIO.LOW)
        GPIO.output(GreenLed, GPIO.LOW)
    if option == auto:
        #run function
return render_template('index.html, **templatedata')
if __name__ == "__main__":
    stoplightctr.run(debug=True, port=80, host='0.0.0.0')
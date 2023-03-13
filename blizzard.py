#Without Button
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
ledPin = 22 #GPIO Pin 22 = Physical Pin 15
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)
try:
	while True:
		GPIO.output(ledPin, True)
		print(“LED ON”)
		sleep(2)
		GPIO.output(ledPin, False)
		print(“LED OFF”)
		sleep(2)
finally:
	GPIO.output(ledPin, False)
	GPIO.cleanup()


#With Button

from gpiozero import LED
from gpiozero import Button

led = LED(4) #declare GPIO pin 4 for LED output and store it in led variable
button = Button(17) #declare GPIO pin 17 for Button output

while True:
	button.wait_for_press()
	led.on()
	button.wait_for_release()
	led.off()


#Stepper Motor
Import RPi.GPIO as GPIO
Import time

GPIO.setmode(GPIO.BOARD)

stepPin1 = 31
stepPin2 = 33
stepPin3 = 35
stepPin4 = 37

GPIO.setup(stepPin1.GPIO.OUT)
GPIO.setup(stepPin2.GPIO.OUT)
GPIO.setup(stepPin3.GPIO.OUT)
GPIO.setup(stepPin4.GPIO.OUT)

GPIO.output(stepPin1, False)
GPIO.output(stepPin2, False)
GPIO.output(stepPin3, False)
GPIO.output(stepPin4, False)

def singleStep(stepVal1, stepVal2, stepVal3, stepVal4):
	GPIO.output(stepPin1, stepVal1)
	GPIO.output(stepPin2, stepVal2)
	GPIO.output(stepPin3, stepVal3)
	GPIO.output(stepPin4, stepVal4)

def clockWiseRotate(delay, steps1):
	for i in range(0, steps1):
		singleStep(1,  0, 0, 0)
		time.sleep(delay)
		singleStep(1,  1, 0, 0)
		time.sleep(delay)
		singleStep(0,  1, 0, 0)
		time.sleep(delay)
		singleStep(0,  1, 1, 0)
		time.sleep(delay)
		singleStep(0,  0, 1, 0)
		time.sleep(delay)
		singleStep(0,  0, 1, 1)
		time.sleep(delay)
		singleStep(0,  0, 0, 1)
		time.sleep(delay)
		singleStep(1,  0, 0, 1)
		time.sleep(delay)


def anticlockWiseRotate(delay, steps2):
	for i in range(0, steps2):
		singleStep(1,  0, 0, 1)
		time.sleep(delay)
		singleStep(0,  0, 0, 1)
		time.sleep(delay)
		singleStep(0,  0, 1, 1)
		time.sleep(delay)
		singleStep(0,  0, 1, 0)
		time.sleep(delay)
		singleStep(0,  1, 1, 0)
		time.sleep(delay)
		singleStep(0,  1, 0, 0)
		time.sleep(delay)
		singleStep(1,  1, 0, 0)
		time.sleep(delay)
		singleStep(1,  0, 0, 0)
		time.sleep(delay)

while 1:
	delay  = input(“Enter delay between steps(in milliseconds): “)
Steps1 = input(“How many steps clockwise: “)
Steps2 = input(“How many steps anticlockwise: “)
clockWiseRotation(int(delay)/1000.0, int(steps1))
anticlockWiseRotation(int(delay)/1000.0, int(steps2))
finally:
	GPIO.cleanup()


#Adafruit

import time
import digitalio
import board
from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_KEY = 'your APIO KEY' # Set your APIO Key
# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'Your Username'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try: 
    digital = aio.feeds('LED')
except RequestError: 
    feed = Feed(name="LED")
    LED = aio.create_feed(feed)
# led set up
led = digitalio.DigitalInOut(board.D6)
led.direction = digitalio.Direction.OUTPUT
while True:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
    elif int(data.value) == 0:
        print('received <- OFF\n')
 
    led.value = int(data.value)

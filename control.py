import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

if sys.argv[-1] == "off":
    GPIO.output(14, GPIO.LOW)

if sys.argv[-1] == "on":
    GPIO.cleanup()

# pwmOut = GPIO.PWM(14, 200)
# pwmOut.start(0)
# dutyCycle = 0
# GPIO.cleanup()

# for i in range(10):
#     time.sleep(0.2)
#     dutyCycle = dutyCycle + 1
#     if(dutyCycle > 100):
#        dutyCycle = 0
#     pwmOut.ChangeDutyCycle(100 - dutyCycle)

# for i in range(100):
#     GPIO.output(14, 6)
#     time.sleep(1)
#     GPIO.output(14, GPIO.LOW)
#     time.sleep(1)


print "Holaaa toquiiiicaaaaaaaaa"
print "Parkourrrrr"
print "ejecutando el programa"

import RPi.GPIO as GPIO
import time
GPIO.VERSION
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)
time.sleep(10)
GPIO.output(7,False)
GPIO.cleanup()

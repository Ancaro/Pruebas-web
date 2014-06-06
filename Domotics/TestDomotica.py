print "\n\tPrimeras pruebas de Domotica con Raspberry Pi"
print "\n\tEste programa me permite seleccionar un tiempo de endendido\n\ty apagado de un Led"
print "\n\tEjecutando el programa"

import RPi.GPIO as GPIO
import time
GPIO.VERSION
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)
time.sleep(10)
GPIO.output(7,False)
GPIO.cleanup()

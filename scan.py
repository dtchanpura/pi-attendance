from time import sleep
import os
import RPi.GPIO as GPIO
from subprocess import *

strpath = "/home/darshil/"
strfile = "webcam"
IRPin=17
LEDRed=22
LEDGrn=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(IRPin,GPIO.IN)
GPIO.setup(LEDRed,GPIO.OUT)
GPIO.setup(LEDGrn,GPIO.OUT)
GPIO.output(LEDGrn,GPIO.LOW);
GPIO.output(LEDRed,GPIO.LOW);

while True:
   if (GPIO.input(IRPin)):
      data=scan()
      # Here goes something to add for Front-end
   else:
      blinkRED() # When nothing is there blink red LED with some predefined period



def capture():
   os.system("sudo fswebcam --device /dev/video0 --input 0 --resolution 352x288 --save "+strpath+strfile+".jpg --skip 2")
def scan():
   scanned=''
   while scanned=='':
      capture()
      scanned=run_cmd("zbarimg "+strpath+strfile+".jpg")
      GPIO.output(LEDRed,GPIO.HIGH);

   GPIO.output(LEDGrn,GPIO.HIGH);
   return scanned

def blinkRED():
   GPIO.output(LEDRed, GPIO.HIGH)
   sleep(0.2)
   GPIO.output(LEDRed, GPIO.HIGH)
   sleep(2)

def run_cmd(cmd):
   p = Popen(cmd, shell=True, stdout=PIPE)
   output = p.communicate()[0]
   return output
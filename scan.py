from time import sleep
import os
import RPi.GPIO as GPIO
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
   os.system("sudo fswebcam --device /dev/video0 --input 0 --resolution 352x288 --save "strpath+strfile".jpg --skip 2")
def scan():
   scanned=1024
   while scanned==1024:
      capture()
      scanned=os.system("zbarimg -q "+strpath+strfile+".jpg")
      GPIO.output(LEDRed,GPIO.HIGH);

   GPIO.output(LEDGrn,GPIO.HIGH);
   return scanned

def blinkRED():
   GPIO.output(LEDRed, GPIO.HIGH)
   sleep(0.2)
   GPIO.output(LEDRed, GPIO.HIGH)
   sleep(2)

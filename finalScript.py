import os

strpath = "/home/darshil/"
strfile = "webcam"
os.system("sudo fswebcam --device /dev/video0 --input 0 --resolution 352x288 --save webcam.jpg --skip 2")
print "Reading data from qrcode"
# call os command to read qr data to text file
print os.system("zbarimg -q "+strpath+strfile+".jpg")


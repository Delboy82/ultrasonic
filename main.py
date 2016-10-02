from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=4) # sets the echo and trigger pins

while True:
   distance=ultrasonic.distance*100
   sleep(0.5)
   
   if distance > 20:
	   print "Everything is ok nothing nearby"
   else:
	   print "looks like there is an object nearby"

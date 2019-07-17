from gpiozero import LED, Button
from time import sleep
#from signal import pause

red = LED(18)
yellow = LED(27)
green = LED(22)
button = Button(2)

red.on()
sleep(1)
red.off()
yellow.on()
sleep(1)
yellow.off()
green.on()
sleep(1)
green.off()

#pause()
#
#while True:
#    button.when_pressed = red.off
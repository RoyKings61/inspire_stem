from machine import Pin
import time


blue_led= Pin(15, Pin.OUT)
Red_led= Pin(16, Pin.OUT)
green_led= Pin(17, Pin.OUT)

blue_led.on()
time.sleep(2)
blue_led.off()

Red_led.on()
time.sleep(2)
Red_led.off()

green_led.on()
time.sleep(2)
green_led.off() 



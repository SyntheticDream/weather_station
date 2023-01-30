from machine import Pin
import utime

def runner():
    led_onboard = Pin("LED", Pin.OUT)
    while True:
        led_onboard.toggle()
        utime.sleep(5)

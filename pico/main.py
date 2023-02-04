import utime
from machine import Pin

led_onboard = Pin("LED", Pin.OUT)

try:
    from runner import runner
    runner()
except Exception as e:
    led_onboard.off()
    while True:
        print(e)
        utime.sleep(10)

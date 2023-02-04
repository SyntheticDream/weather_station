import utime
from machine import Pin

def read_bme688():
    from breakout_bme68x import BreakoutBME68X
    from pimoroni_i2c import PimoroniI2C

    PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

    i2c = PimoroniI2C(**PINS_PICO_EXPLORER)
    bme = BreakoutBME68X(i2c)

    led_onboard = Pin("LED", Pin.OUT)
    while True:
        print("reading sensor")

        temperature, pressure, humidity, gas_resistance, status, gas_index, meas_index = bme.read()

        print(temperature, pressure, humidity, gas_resistance, status, gas_index, meas_index)

        led_onboard.toggle()
        utime.sleep(5)

def runner():
    read_bme688()

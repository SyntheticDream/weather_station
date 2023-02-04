# weather_station
Raspberry Pico W based weather station

## requirements

Custom pimoroni MicroPython image is needed for BME688 breakout - https://github.com/pimoroni/pimoroni-pico/releases/latest/.

After you flush the image you can go ahead and manually upload files from pico folder to Pico-W via Thonny.
Otherwise, for automatic sync you would need:

* python3.10
* make
  * or **Pico-W-Go** extension for VSCode. You will need to set `pico` as sync folder in `.vscode/settings.json` after project initiation.

## deploy

Connect Pico via USB and use preferred sync method.

### using make
``` bash
#set AMPY_PORT=COM7         -- example for windows
#export AMPY_PORT=/dev/tty  -- example for linux

pip install -r requirements.txt
make cp
```

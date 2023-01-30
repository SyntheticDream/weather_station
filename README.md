# weather_station
Raspberry Pico W based weather station

## requirements

Pico-W-Go extension for VSCode
python3.10
make

## dev setup

Install and initiate Pico-W-Go extension. Choose `pico` as sync folder.

## build

``` bash
#set AMPY_PORT=COM7         -- example for windows
#export AMPY_PORT=/dev/tty  -- example for linux

pip install -r requirements.txt
make put
```

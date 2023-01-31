# weather_station
Raspberry Pico W based weather station

## requirements

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

### using VSCode 
sync via **Pico-W-Go**

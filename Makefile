all: put

rm:
	ampy rm main.py
	ampy rm runner.py
put: pico/main.py pico/runner.py
	ampy put pico/main.py
	ampy put pico/runner.py

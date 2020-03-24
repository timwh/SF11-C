#!/usr/bin/env python3
### Python3 serial for Lightware SF11/C laser rangefinder on RPi
# uses ttyUSB0 - change as required to relevant serial port
### Tim Whiteside

### Library###
import serial
from time import sleep
# Open port
ser2 = serial.Serial("/dev/ttyUSB0",115200,8,'N',1,timeout=0.5)
# Run program
while True:
    data2 = ser2.readline()  # read LiDAR stream
    data2 = data2.decode("utf-8") # turn from byte to string
    print(data2) # display output
    sleep(0.05) #50 ms between readings


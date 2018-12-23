#!/usr/bin/env python

import time
import os,sys

SENSOR_PORT = "/dev/ttyUSB0"

fd = os.open(SENSOR_PORT,os.O_RDWR|os.O_NOCTTY)
print(os.write(fd,"ruok\n".encode()))
time.sleep(1)
print(os.read(fd,256))
os.close(fd)
sys.exit()

with open(SENSOR_PORT,"r+") as port:
    try:
        while(True):
            port.write("temp\n")
            t = port.readline()
            print("Temperature read: " + t)
            time.sleep(3)
    except:
        pass

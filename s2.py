#!/usr/bin/env python

import serial
import time

s = serial.Serial('/dev/ttyUSB0',9600)

print(s.name)

print(s.readline())

while(True):
    s.write(b"humid\n")
    print(s.readline())
    s.write(b"temp\n")
    print(s.readline())
    s.write(b"ruok\n")
    print(s.readline())
    time.sleep(1)

s.close()


#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1);

try:
    while 1:
        rawdata = ser.readall();
        if (len(rawdata) > 3):
            data = rawdata.decode();
            print(data);
except:
        ser.close();
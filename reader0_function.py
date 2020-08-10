#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1);

r0=[0, 0, 0, 0]
try:
    while 1:
        rawdata = ser.readall()
        if (len(rawdata) > 3):
            data = rawdata.decode()
        def return_data():
            reture (r0)
            #def return_data():                
            #    return data
except:
    ser.close();
    
    
#!/usr/bin/env python
#import serial
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1);

#def return_data():
#    rawdata = ser.readall()
#    print("raw",rawdata)
#    if ("[" in rawdata):
#        data = rawdata.decode()
#        print("deocde",data)
#        return data
# ser.close();


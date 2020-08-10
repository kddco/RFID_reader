#!/usr/bin/env python
import serial

class Read():
    def __init__(self, id):
        self.id=id
        ser = serial.Serial('/dev/ttyUSB'+str(id), 9600, timeout=1);
    def get(self):
        r0 = [0, 0, 0, 0]
        try:
            while 1:
                rawdata = ser.readall()
                if (len(rawdata) > 3):
                    result_data = rawdata.decode()
                    return (result_data)

        except Exception:
            ser.close()
            print("USB", id , Exception)


    
    
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


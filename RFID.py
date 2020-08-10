#!/usr/bin/env python
import serial

class Read():
    def __init__(self, id):
        self.id=id
        self.ser = serial.Serial('/dev/ttyUSB'+str(id), 9600, timeout=1);
        print("self.ser",self.ser)
        print("USB",id,"init ok")
    def get(self):
        while(1):
            try:
                rawdata = self.ser.readall()
                if (len(rawdata) > 3):
                    result_data = rawdata.decode()
                    print("result:",result_data)
                    return (result_data)
                else:
                    print("get nothing")
            except Exception:
                self.ser.close()
                print("USB", id , Exception)

if __name__ == '__main__':
    r= Read("1")
    r.get()
    
    
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


class Reader():
    def __init__(self, id):
        self.id=id
        self.ser = "hello"
    def get(self):
        print(self.ser)


r= Reader(2)
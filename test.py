class Read():
    def __init__(self, id):
        self.id=id
        self.ser = "serser"
    def get(self):
        print(self.ser)

r= Read(2)
r.get()
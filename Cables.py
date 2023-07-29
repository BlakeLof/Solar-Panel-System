#Cables is a child class of equipment
#Cables will be used to check that all equipment are plugged in and connected
class Cables(Equipment):
    
    def __init__(self, name, type, temp, status):
        super().__init__(name, type)
        self.temp = temp
        self.status = status
    
    def get_status(self):
        print(self.status)
        
    def set_status(self, status):
        self.status = status
    
    def get_temp(self):
        print(self.temp)
        
    def set_temp(self, temp):
        self.temp = temp
        
    #functions to check that equipment are responsive
    #Functions to send an error that equipment is disconnected
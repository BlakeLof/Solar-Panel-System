#Controller is a child class of equipment
#Controller will be the main brain of controlling the other equipment
class Controller(Equipment):
    
    def __init__(self, name, type, position, temp, status):
        super().__init__(name, type)
        self.position = position
        self.temp = temp
        self.status = status
    
    def get_position(self):
        print(self.position)
        
    def set_position(self, position):
        self.position = position
    
    def get_status(self):
        print(self.status)
        
    def set_status(self, status):
        self.status = status
    
    def get_temp(self):
        print(self.temp)
        
    def set_temp(self, temp):
        self.temp = temp
        
    #functions to check status and temp of the equipment
    #Functions to control motors
    #functions to control battery capacity
    #Functions to check solarpanel visibility
    
        
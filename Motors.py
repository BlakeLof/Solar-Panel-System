#Motor is a child class of equipment
#Motor will be used to reposition the solarpanels for most visibility
class Motors(Equipment):

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
        
    #Functions to control motor rotation
    
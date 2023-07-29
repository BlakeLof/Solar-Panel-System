
#Battery is a child of Equipment
#This class will be in charge of the battery component
class Battery(Equipment):
    
    def __init__(self, name, type, capacity, temp, status):
        super().__init__(name, type) #equipment variables
        self.capacity = capacity
        self.temp = temp
        self.status = status
    
    
    def get_capacity(self):
        print(self.capacity)
        
    def set_position(self, capacity):
        self.capacity = capacity
    
    def get_status(self):
        print(self.status)
        
    def set_status(self, status):
        self.status = status
    
    def get_temp(self):
        print(self.temp)
        
    def set_temp(self, temp):
        self.temp = temp
        
        
 #add functions to track battery capacity, temp, and status of the battery
 #add failsafe incase battery is either full or integrity failure
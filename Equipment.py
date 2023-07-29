#Main parent class, all equipment will be stored under this class
class Equipment:
    
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
        
    def name(self): #Each equipment will have its own designated name ie Motor1 and Motor2
        print(self.name)
        
    def type(self): #What type of equipment it is
        print(self.type)
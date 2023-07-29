#Solar Panels is a child class of equipment
#Solar Panels is the main concern of the system, and will be focused on the overall coverage by the solar panels

class SolarPanels(Equipment):

    def __init__(self, name, type, temp, output, status):
        super().__init__(name, type)
        self.temp = temp
        self.output = output
        self.status = status
           
    def setTemp(self, temp):
        self.temp = temp
        
    def getTemp(self):
        print(self.temp)
    
    def setOutput(self, output):
        self.output = output
    
    def getOutput(self):
        print(self.output)
        
    def setStatus(self, status):
        self.status = status
        
    def getStatus(self):
        print(self.status)
        
    #Function to get information from light sensors
    #Function to calculate total output of the solar panels power
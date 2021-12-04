class Car:
    wheels = 4  #class variable you can make it default

    def __init__(self,make,model,year,color):
        self.make = make  #instance variable
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print("The "+self.make+" car is driving")
    def stop(self):
        print("The "+self.make+" car has stopped")
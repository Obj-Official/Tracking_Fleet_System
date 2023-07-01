import random

#tracking fleet class
class TrackingFleet:
    
    #initializer
    def __init__(self, numOfCars):
        self.number = numOfCars
        self.latitudeLow = 6.5115
        self.latitudeHigh = 6.5195
        self.longitudeLow = 3.3935
        self.longitudeHigh = 3.3855
        self.car1 = []
        self.car2 = []
        self.car3 = []
        self.car4 = []
        self.cars = [self.car1, self.car2, self.car3, self.car4]
        self.driven = 0
        
    #method to define the cars randomly and their exact location in unilag
    def defineCar(self):
        carColor = ["Red ", "Silver ", "Purple ", "White ", "Orange "]
        carType = ["Toyota", "volkswagen", "Bentley", "Benz", "Bughatti"] 
        x = 0
        itemIndex = 0
        carLatitude = 0
        carLongitude = 0
        self.driven = 0
        while x < self.number:
                self.cars[x].append(x+1)       
                itemIndex = random.randint(0,4)
                self.cars[x].append(carColor[itemIndex])
                itemIndex = random.randint(0,4)
                self.cars[x].append(carType[itemIndex])
                self.cars[x].append(" REG" + str(random.randint(1000,9999)))
                carLatitude = round(random.uniform(self.latitudeLow, self.latitudeHigh),4)
                self.cars[x].append(carLatitude)
                carLongitude = round(random.uniform(self.longitudeLow, self.longitudeHigh),4)
                self.cars[x].append(carLongitude)
                x += 1
       
    
    #driving method which changes the car's location, giving a simulation of the car driving
    def driveCar(self):
        oldCarLatitude = 0
        oldCarLongitude = 0
        self.driven = 1
        for x in range(0,self.number):
            oldCarLongitude = self.cars[x].pop()
            oldCarLatitude = self.cars[x].pop()
            newCarLatitude = round(random.uniform(self.latitudeLow, self.latitudeHigh),4)
            self.cars[x].append(newCarLatitude)
            newCarLongitude = round(random.uniform(self.longitudeLow, self.longitudeHigh),4)
            self.cars[x].append(newCarLongitude)
            
    def trackCar(self):
        for x in range (0, self.number):
            if x == 0:
                print("\nCar " + str(self.car1[0])+ ": " + self.car1[1] + self.car1[2] + self.car1[3] + " \n" + "Location: " + str(self.car1[4]) + "°N " + str(self.car1[5]) + "°E\n")
            elif x == 1:
                print("Car " + str(self.car2[0])+ ": " + self.car2[1] + self.car2[2] + self.car2[3] + " \n" + "Location: " + str(self.car2[4]) + "°N " + str(self.car2[5]) + "°E\n")
            elif x == 2:
                print("Car " + str(self.car3[0])+ ": " + self.car3[1] + self.car3[2] + self.car3[3] + " \n" + "Location: " + str(self.car3[4]) + "°N " + str(self.car3[5]) + "°E\n")
            elif x == 3:
                print("Car " + str(self.car4[0])+ ": " + self.car4[1] + self.car4[2] + self.car4[3] + " \n" + "Location: " + str(self.car4[4]) + "°N " + str(self.car4[5]) + "°E\n")

#main function
def main():
    print("Tracking fleet vehicles v1.0.1\n\n")
    correctValue = 0
    valueEntered = 0
    alreadyDefined = 0
    #This loop and the  following conditional statement ensures you enter correct value(number of car)
    while correctValue == 0:
        number = eval(input("Input the number of cars operating in the tracking system (Between 2 and 4): "))
        if (number >= 2) and (number <=4 ):
            correctValue = 1
            #This loop keeps the program alive until the user enters a sentinel value to terminate program 
            while valueEntered != 3: 
                if alreadyDefined == 0:
                    carObjects = TrackingFleet(number)
                    carObjects.defineCar()
                    carObjects.trackCar()
                    alreadyDefined = 1
                valueEntered = eval(input("Enter 1 to drive car (change current location)\nEnter 2 to track car's current location\nEnter 3 to terminate Tracking system:\n"))
                if valueEntered == 1:
                    carObjects.driveCar()
                    print("\nThe cars have moved, check current location\n")
                elif valueEntered == 2:
                    print("\nCurrent car location")
                    carObjects.trackCar()
                
main()       

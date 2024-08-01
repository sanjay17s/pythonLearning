class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0
    
    def describeCar(self):
        print(f"It's a {self.make} {self.model} {self.year}")
    
    def getOdometerReading(self):
        return self.odometerReading
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometerReading = mileage

# Creating an instance of Car
my_car = Car('Toyota', 'Corolla', 2020)
my_car.update_odometer(23)

# Using the instance method to get the odometer reading
print(my_car.getOdometerReading())

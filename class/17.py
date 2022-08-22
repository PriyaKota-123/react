#7.define a property that must have the same value for every class instance(object).

class vehicle():
    color="white"
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class Bus(vehicle):
    pass
class car(vehicle):
    pass
b=Bus("volo",180,20)
print(b.color,"vehicle name:",b.name,"speed:",b.speed,"mileage:",b.mileage)
car=car("BMW",240,18)
print(car.color,car.name,"speed:",car.speed,"mileage:",car.mileage)
    

'''RaceCar


Now we need a RaceCar in our cars world

You are given two  classes Car and RaceCar

A Race Car is a Car but with the additional behaviours'

Inherit the Car class into RaceCar Class and build the additional features

implement the car and RaceCar classes with described attributes and methods


RaceCar have following attributes and methods
Attributes:
color,max_speed,acceeleration,tyre_friction,is_engine_started,current_speed,nitro
note: nitro is race_car attributes as child attribute

Methods:
start_engine,stop_engine,accelerate,apply_breaks,sound_horn

override Methods:
1. sound_horn:
   print peeppeep or beep beep if Race_car engine is on 
   print car has not started yet if Race_car engine is off

2.accelerate:
    when car accelerates when nitro points are available the current_spped will be add 20 within max limits and nitro get reduced by 1 point 



racecar = color:"red",max_speed=250,acceleration =50,tyre_friction=30,nitro=4'''



class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.current_speed=0

    def start_engine(self):
        self.is_engine_started=True
        



    def stop_engine(self):
        self.is_engine_started=False


    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started Yet")
        else:
            self.current_speed +=self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed=self.max_speed


    def apply_breaks(self):
        self.current_speed -=self.tyre_friction
        if self.current_speed < 0:
            self.current_speed=0


    def sound_horn(self):
        if self.is_engine_started:
            print("BEEP BEEP")
        else:
            print("CAR HAS NOT STARTED YET")



class RaceCar(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,nitro):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.nitro=nitro

    def accelerate(self):
        if self.nitro > 0 and self.is_engine_started:
            self.current_speed +=20
            self.nitro -=1
        super().accelerate()
        
    def sound_horn(self):
        if self.is_engine_started:
            print("BEEP BEEP")
        else:
            print("CAR HAS NOT STARTED YET")

    
racecar = RaceCar(color="red",max_speed=250,acceleration =50,tyre_friction=30,nitro=4)
racecar.start_engine()
racecar.accelerate()
print(racecar.current_speed)
print(racecar.nitro)
racecar.accelerate()
print(racecar.current_speed)
print(racecar.nitro)
racecar.apply_breaks()
print(racecar.current_speed)
print(racecar.nitro)
racecar.accelerate()
print(racecar.current_speed)
print(racecar.nitro)
print(racecar.sound_horn())
    

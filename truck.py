##Univariate quadratic polynomials are the most common polynomials. 
##Polynomials with only one unknown number and the highest degree of 2 are called univariate quadratic polynomials.
## Its standard form is ax^2+bx+c
##Please complete the code in solution.py to realize the function of equation.
##The equation function receives three parameters a, b, and c as the quadratic term, the primary term, and the constant term of the standard form of a bivariate quadratic polynomial. 
##Please use the lambda function to pass in an unknown number x for the equation function and take this lambda function as the return value of the equation function. 
##Find the result of the univariate quadratic polynomial ax^2+bx+c
##
##Example
##The quizzer runs main.py by executing python main.py {input_path} , which outputs the updated string after running, and you can see how the code is running in main.py.
##
##Example 1
##
##Input:
##2 3 7
##3
##Output:
##
##34
##
##
##Explanation:
##After passing in the first row of parameters, the expression is 2x^2+3x+7
##
##When x=3 the result of the expression is 34
##
##Example 2
##
##Input:
##
##1 2 0
##5
##Output:
##
##35
##Explanation:
##After passing in the first row of parameters, the expression is x^2+2x+0
##When x=5 the result of the expression is 35




class Car:
    def __init__(self,color,max_speed,acceeleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceeleration=acceeleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.current_speed=0

    def start_engine(self):
        self.is_engine_started = True
        
    def  stop_engine(self):
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
            print("Car has not started Yet")
            
class Truck(Car):
    def __init__(self,color,max_speed,acceeleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceeleration,tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self.load =0

    def sound_horn(self):
        if self.is_engine_started:
            print("honk houk")
        else:
            print("Car has not started Yet")
    def stop_engine(self):
        super().stop_engine()
    def load_cargo(self,cargo_weight):
        if self.is_engine_started:
            print("can not load during motion")
        elif cargo_weight +self.load>self.max_cargo_weight:
            print("can not load cargo more than Maxlimit:{}".format(self.max_cargo_weight))
        else:
            self.load+=cargo_weight
    def unload_cargo(self,cargo_weight):
        if self.is_engine_started:
            print("can not unload during motion")
        else:
            self.load-=cargo_weight
            if self.load<0:
                self.load=0
truck = Truck(color="Blue",max_speed=340,acceeleration=40,tyre_friction=30,max_cargo_weight=18000)
truck.load_cargo(cargo_weight=1200)
print(truck.load)
truck.unload_cargo(cargo_weight=800)
print(truck.load)
truck.load_cargo(cargo_weight=12000)
truck.sound_horn()
truck.stop_engine()

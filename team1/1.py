##1.Create a class Teacher with name, age, and salary attributes,
##where salary must be a private attribute that cannot be accessed outside the class.



##class Teacher():
##    def __init__(self,name,age,salary):
##        self.name=name
##        self.age=age
##        self.__salary=salary
##    def display(self):
##        print("name: ",self.name)
##        print("age: ",self.age)
##        print("salary: ",self.__salary)
##
##s=Teacher("priya",22,2234)
##s.display()
##
##
##        

    

class Teacher():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
s=Teacher("priya",22,25000)
print(s.name)
print(s.age)
print(s.salary)

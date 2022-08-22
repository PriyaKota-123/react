
#3.write a program on single inheritance
class father():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
##    def display(self):
##        print(self.name)
##        print(self.age)
##        print(self.gender)
class son(father):
    def __init__(self,name,age,gender,surname):
        self.surname=surname
        super().__init__(name,age,gender)
a=son("uday",45,"male","kota")
print(a.name)
print(a.surname)
print(a.age)
print(a.gender)

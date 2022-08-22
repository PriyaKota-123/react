#2.WAP on Duck type polymorphism. with example


class Animals():
    def eat(self):
        print("lion is an wild")
    def talk(self):
        print("Hooooooo")

    def walk(self):
        print("running")
class birds():
    def eat(self):
        print("it is a bird")
    def talk(self):
        print("RARAsd")
    def walk(self):
        print("fly in sky")
obj=Animals()
obj1=birds()
##for A in (obj,obj1):
##    A.talk()
##    A.walk()
##    A.eat()
##

def fun(obj):
    obj.eat()
    obj.talk()
    obj.walk()
    
fun(obj)
fun(obj1

#1.Define Multiple inheritance and write an example?

'''class uncle():
    def __init__(self,name):
        self.name=name
    def fun(self):
        print("uncle name:",self.name)
class aunty():
    def __init__(self,surname):
        self.surname=surname
    def fun1(self):
        print("aunty surname:",self.surname)
class daughter(uncle,aunty):
    def __init__(self,name,surname,gender):
        self.gender=gender
        aunty.__init__(self,surname)
        uncle.__init__(self,name)
        
    def fun2(self):
        print("",self.name)
        print("",self.surname)
        print("",self.gender)
        
s=daughter("john","kota","female")
s.fun2()
s.fun1()
s.fun() '''



#2.WAP on Duck type polymorphism. with example


'''class Animals():
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
fun(obj1)'''

#3.demonstrate strong typing method in polymorphism with example


'''class Animals():
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
##obj=Animals()
##obj1=birds()
##for A in (obj,obj1):
##  A.talk()
##  A.walk()
##  A.eat()
def fun(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
    if hasattr(obj,'eat'):
        obj.eat()
a=Animals()    
fun(a)
b=birds()
fun(b)'''


#4.write a program Russian Multiplication using class and object


'''class multi:
    def russian(self,a,b):
        res=0
        while b>0:
            if b&1:
                res=res+a
            a=a<<1
            b=b>>1
        return res
obj=multi()
print(obj.russian(4,5))'''


#5.write a program about ojas organization parent class is ojas and child class is OILC write differnt batches as methods define batchs name with inheritance.

'''class ojas():
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal
    def show(self):
        print("name:",sef.name)
        print("id:",self.id)
        print("sal:",self.sal)
class oilc():
    def __init__(self,name,id,sal,des):
        self.des=des
        super().__init__(name,id,sal)
    def show1(self):
        print("name",self.name)
        print("id",self.id)
        print("sal",self.sal)
        print("des",self.des)
obj=oilc("priya",22,22345,"hyd")
obj.show()
obj.show1()'''



'''s1=input("Enter a String:")
s2=input("Enter a String:")
output=""
i=0
j=0
a=[]
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output+=s1[i]
        i=i+1
    if j<len(s2):
        output+=s2[j]+","
        j=j+1
    a.append(output)

print(a)'''



a=b"kota priya"
print(a)
for i in a:
    print(i)






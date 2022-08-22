#polymorphism 

'''class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()'''



#polymorphism with Duck typing


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



#polymorphism with strong typing

'''class rose():
    def color(self):
        print("rose in red color")
    def falvour(self):
        print("it is good")
class apple():
    def color(self):
        print("it is in red color")
    def falvour(self):
        print("it is good ")
def fun1(obj):
    if hasattr(obj,'color'):
        obj.color()
    if hasattr(obj,'falvour'):
        obj.falvour()
r=rose()
fun1(r)
a=apple()
fun1(a)'''


# This Method Overloading Concept is not available in Python
# So it will show error
'''class Myclass:
	def sum(self, a):
		print("1st Sum Method", a)
		
	def sum(self):
		print("2nd Sum Method")		
		
obj = Myclass()
obj.sum()
obj.sum(10)'''

#method overloading show error

'''class girl():
    def rose(self,a):
        print("rose flower")
    def rose(self):
        print("rose flower is beautiful")
obj=girl()
obj.rose()
obj.rose(4)'''


# Method Overloading
'''class Myclass:
	def sum(self, a=None, b=None, c=None):
		if a!=None and b!=None and c!=None:
			s = a + b + c
		elif a!=None and b!=None:
			s = a + b
		else:
			s = 'Provide at least Two Numbers'
		return s
		
obj = Myclass()
print(obj.sum(10, 20, 30))
print(obj.sum(90,10))
print(obj.sum())'''


#example with method overloading


'''class vicky():
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        return s
d=vicky()
print(d.add(10,40,70))
print(d.add(60,70))'''


# Method Overriding
'''class Add:
	def result(self, a, b):
		print('Addition:', a+b)
		
class Multi(Add):
	def result(self, a, b):
		print('Multiplication:', a*b)
		
m = Multi()
m.result(10, 20)

m = Add()
m.result(10, 20)'''



#example of method overriding

'''class sub:
    def S(self,a,b):
        print("sub:",a-b)
class add:
    def A(self,a,b):
        print("add:",a+b)
obj=sub()
obj.S(120,40)
obj=add()
obj.A(345,678)'''


# Method Overriding with super()
'''class Add:
	def result(self, a, b):
		print('Addition:', a+b)
		
class Multi(Add):
	def result(self, a, b):
		super().result(10, 20)				# Calling Parent Class's Method
		print('Multiplication:', a*b)
		
m = Multi()
m.result(10, 20)'''


#example with super method()

'''class add:
    def A(self,a,b):
        print("string",a+b)
class sub(add):
    def A(self,a,b):
        super().A(10,30)
        print("sub",a-b)
obj=sub()
obj.A(1,9)'''

# Operator Overloading
'''class A:
	def __init__(self, x):
		self.x = x
	def __add__(self, other):
		return self.x + other.x
			
class B:
	def __init__(self, x):
		self.x = x
		
a = A(100)
b = B(200)
print(a+b)'''	    



#example operator overloading

'''class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x + other.x
class B:
    def __init__(self,x):
        self.x=x
##a=A(100)
##b=B(200)
##print(a+b)

A.__add__(a,b)
int.__add__(10,20)
str.__add__('a','b')
A.__add__(a,b)'''

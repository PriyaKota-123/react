'''1) wap to create class and create two objects from that class and add those two objects using _add_ (operator overloading)''' 


##class A:
##    def __init__(self,a):
##        self.a=a
##    def __add__(self,b):
##        return self.a+self.b
##class B:
##    def __init__(self,b):
##        self.b=b
##int.__add__(10,20)
##str.__add__('a','b')
##A.__add__(a,b)


##class add():
##    def __init__(self,a):
##        self.a=a
##    def __add__(self,b):
##        return self.a+b.a
##a=add(8)
##b=add(9)
##print(a+b)


'''2) wap to create a generator by using send method'''


##def hello(n):
##    a=yield
##    while a<n:
##        a=yield a
##        a=a+1
##f=hello(10)
##next(f)
##print(f.send(1))
##print(f.send(8))
##print(f.send(7))



'''3) wap to create the generator comprehension'''

##def fun():
##    x=[i for i in range(10) if i%2==0]
##    yield x
##for j in fun():
##    print(j)


'''4) print a function n number of times using decorator'''

##def fun(b):
##    def fun1(a):
##        return b(a)
##    return fun1
##@fun
##def add(a):
##    for i in range(a):
##        print('hello')
##add(a=int(input("enter a number")))


'''5) write a python program to check the how many instance variables are there in a class.'''

##class A:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def add(self,c,d):
##        self.c=c
##        self.d=d
##s=A(1,2)
##s.add(3,4)
##print(s.__dict__)
##print(len((s.__dict__)))



































class rose():
    def color(self):
        print("red")
    def fal(self):
        print("good")
class apple():
    def color(self):
        print("red")
    def fal(self):
        print("good")

def fun(obj):
    if hasattr(obj,'color'):
        obj.color()
    if hasattr(obj,'fal'):
        obj.fal()
r=rose()
fun(r)
a=apple()
fun(a)
#======================================
'''class my:
    def sum(self,a):
        print("1st sum",a)
    def sum(self):
        print("2nd sum",a)
obj=my()
obj.sum()
obj.sum(10)'''
#=================================================
'''class sub:
    def s(self,a,b):
        print("sub",a-b)
class add(sub):
    def s(self,a,b):
       print("add",a+b)
obj=sub()
obj.s(23,6)
obj=add()
obj.s(12,14)'''

#=================================================
'''class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x
class B:
    def __init__(self,x):
        self.x=x
a=A(100)
b=B(200)
print(a+b)
A.__add__(a,b)
int.__add__(10,20)
str.__add__('a','b')
A.__add__(a,b)'''
#================================

'''class uncle():
    def __init__(self):
        self.sal=9000
    def fun(self):
        print("uncle salary:",self.sal)
class aunty():
    def __init__(self):
        self.sal=67889
    def fun1(self):
        print("aunty salary:",self.sal)
class daughter(uncle,aunty):
    def __init__(self):
        self.sal=56778
        self.name="priya"
    def fun2(self):
        print("daughter salary:",self.sal)
s=daughter()
print(s.sal)
print(s.name)
s.fun2()
s.fun1()
s.fun()'''


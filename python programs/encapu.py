'''class base:
    def __init__(self):
        self._a=2
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("calling procted member",self._a)
        self._a=3
        print("calling modified ",self._a)
obj=derived()
obj1=base()
print("acessing",obj._a)
print("acessing",obj1._a)'''


'''class base:
    def __init__(self):
        self.a="priya"
        self.__c="priya"
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("")
        print(self.__c)
obj=base()
print(obj.a)'''


'''class priya:
    def __init__(self):
        self.a="priya"
        self.__c="priya"
class picky:
    def __init__(self):
        priya.__init__(self)
        print(self.__c)
obj=base()
print(obj.a)'''


'''class base:
    __a=20
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def hello(self):
        print(self.a)
        print(self.b)
        print(self.__a)
    
b=base(10,20)
b.hello()'''


'''class base:
    __b=70
    def __init__(self,__name):
        self.__name=__name
    def hi(self):
        print(self.__name)
        print(self.__b)
h=base("priya")
h.hi()'''



#============================================================================
#setattr
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print("ID",self.id)
        print("Name",self.name)
s=Student(22114,"Mounika")
s.display()
s.__setattr__("grade","A")
print(s.grade)
#==================================================
#getattr
class p:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("name",self.name)
s=p("priya")
s.display()
s.__setattr__("grade","A")
d=getattr(s,"grade")
print(d)
print(s.grade)
#======================================================


class s:
    def display(self):
        self.a=a
    def s(self):
        self.b=b
d=s(10)
d.display()
d.__setattr__()
        

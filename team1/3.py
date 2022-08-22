#3.How to copy all properties of an object to another object in Python?

##class object():
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def obj(self):
##        a={"priya":22}
##        b={"kota":1}
##        super().__init__(a,b)
##obj1=obj.__dict__.copy()
##print(obj1.a)
##print(obj1.b)
##
##
##
##




class object():
    def __init__(self):
        super(object,self).__init__()
        self.f=10
        self.b=20
obj1=object()
obj2=object()
obj1.f=25
obj2.__dict__.update(obj1.__dict__)
print(obj1.f)
print(obj2.f)





        

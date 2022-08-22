
#2.WAP instance method,static method,class method using some example.

class student():
    def __init__(self,name,id,exp):
        self.name=name
        self.id=id
        self.exp=exp
p=student("priya",6,6)
print(p.name)
print(p.id)
print(p.exp)



class car():
    def __init__(cls,name,model):
        cls.name=name
        cls.model=model
c=car("kia",444)
print(c.name)
print(c.model)


class calculate():
    def add(x,y):
        return x+y
calculate.add=staticmethod(calculate.add)
print(calculate.add(5,7))

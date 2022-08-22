
#2.Write a Python class Square, and define two methods that return the square area and perimeter

class square():
    def __init__(self,a):
        self.a=a
    def display(self):
        a=2
        A=a*a
        print(A)
    def display1(self):
        a=2
        p=4*a
        print(p)
s=square(2)
s.display()
s.display1()

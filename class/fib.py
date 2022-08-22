

#4.WAP fibonacci series using oops concept.

##class fib():
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def display(self):
##        a=0
##        b=1
##        
##        for i in range(1,10):
##            c=a+b
##            a=b
##            b=c
##            print(c)
##F=fib(a=int(input("enter a number")),b=int(input("enter a number")))
##F.display()

class fib():
    def __init__(self,n):
        self.a=0
        self.b=1
        self.n=n
    def display(self):
        a=0
        b=1
        for i in range(1,self.n):
            c=a+b
            a=b
            b=c
            print(c)
F=fib(10)
F.display()

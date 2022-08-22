##4.Create a method called Factorial() which allows to calculate the factorial of an integer.
##Test the method by instantiating the class.


class fact1():
    def __init__(self,a):
        self.a=a
    def display(self):
        fact=1
        for i in range(1,self.a+1):
            fact=fact*i
            print(fact)
f=fact1(a=int(input("enter a number")))
f.display()
        

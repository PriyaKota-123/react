#5.WAP on armstrong using oops concepts

class arm():
    def __init__(self,a):
        self.a=a
    def display(self):
        sum=0
        b=len(self.a)
        for i in self.a:
            c=int(i)
            sum=sum+(c**b)
        d=int(self.a)
        if d==sum:
                print("it is an armstrong")
        else:
            print("not")

A=arm(a=input("enter a number"))
A.display()

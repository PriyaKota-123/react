#1.write a python program using oops concept finding prime number or not


class Prime:
    def __init__(self,a):
        self.a=a
    def num(self):
        print(self.a)
        for i in range(2,self.a):
            if self.a%i==0:
                print("not")
                break
        else:
            print("prime number")
p=Prime(a=int(input("enter a number")))
p.num()

#1.write a pythonprogram  using oops concept finding prime number or not.


class prime():
    def __init__(self,a):
        self.a=a
        for i in range(2,a):
            if self.a%i==0:
                print("not")
                break
        else:
            print("prime")
p=prime(a=int(input("enter a number")))


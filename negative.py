##def fun(a):
##    def fun1():
##        n=int(input("enter a value"))
##        if n>0:
##            print("it is positive")
##        else:
##            print("it is negative")
##    return fun1
##def fun3():
##    pass
##r=fun(fun3)
##r()
##
##def fun(a):
##    def fun1():
##        n=int(input())
##        b=len(str(n))
##        sum=0
##        temp=n
##        while(temp>0):
##            c=temp%10
##            sum=sum+c**b
##            temp=temp//10
##        if n==sum:
##            print("it is arm")
##        else:
##            print("not")
##    return fun1
##def fun3():
##    pass
##r=fun(fun3)
##r()


##def fun(a):
##    def fun1():
##        n=int(input())
##        fact=1
##        for i in range(1,n+1):
##            fact=fact*i
##        print(fact)
##    return fun1
##def fun3():
##    pass
##r=fun(fun3)
##r()        
##        
##def fun(a):
##    def fun1():
##        n=int(input())
##        if n%2==0:
##            print("even")
##        else:
##            print("odd")
##    return fun1
##def fun3():
##    pass
##r=fun(fun3)
##r()


##def fun(a):
##    def fun1():
##        n=int(input("enter a value"))
##        i=1
##        sum=0
##        while(i<n):
##            if n%i==0:
##                sum=sum+i
##            i=i+1
##        if n==sum:
##            print("perfect")
##        else:
##            print("not")
##    return fun
##def fun3():
##    pass
##r=fun(fun3)
##r()


##def fun(a):
##    def fun1():
##        n=int(input("enter a value"))
##        count=0
##        for i in range(1,n+1):
##            if n%i==0:
##                count=count+1
##        if count==2:
##                print("prime")
##        else:
##            print("not")
##    return fun1
##def fun2():
##    pass
##r=fun(fun2)
##r()
##
##def fun(a):
##    def fun1():
##        n=int(input("enter a value"))
##        sum=0
##        temp=n
##        while(temp>0):
##            c=temp%10
##            sum=sum*10+c
##            temp=temp//10
##        if sum==n:
##            print("palindrome")
##        else:
##            print("not")
##    return fun1
##@fun
##def fun2():
##    pass
###r=fun(fun2)
##fun2()

##
##def fun(x,y):
##    def fun1():
##        if x > y:
##            greater=x
##        else:
##            greater=y
##        while(True):
##            if((greater % x == 0)and(greater % y == 0)):
##                lcm=greater
##                break
##            greater +=1
##        print(lcm)
##    return fun1()
##x=54
##y=24
##fun(x,y)
##
##
##def fun(x,y):
##    def fun1():
##        if x > y:
##            greater=x
##        else:
##            greater=y
##        while(True):
##            if((greater % x == 0)and(greater % y == 0)):
##                lcm=greater
##                break
##            greater +=1
##        print(lcm)
##    return fun1
##x=4
##y=6
##fun(x,y)

def fun(a):
    def fun1():
        n=int(input(""))
        sum=0
        temp=n
        while(n>0):
            fact=1
            c=n%10
            for i in range(1,c+1):
                fact=fact*i
            sum=sum+fact
            n=n//10
        if temp==sum:
                print("it is a strong")
        else:
            print("not")
    return fun1()
def fun2():
    pass
r=fun(fun2)
r




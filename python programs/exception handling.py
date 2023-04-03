#TryExceptElse example
'''a=10
b=0
try:
    d=a/b
    print(d)
    print("inside try")
except ZeroDivisionError:
    print("division by zero not allowed")
else:
    print("inside else")
print("rest of code")

output:
division by zero not allowed
rest of code'''

#Except

'''a=10
b=0
try:
    d=a/b
    print(d)
except:
    print("exception handler")
print("rest of the code")'''


'''a=int(input(""))
for i in range(2,a):
    if a%i==0:
        print("not a prime")
    else:
        print("it is prime number")
try:
    print("range of the value")
except:
    print("exception handling")
finally:
    print("code finished")

output:

5
it is prime number
it is prime number
it is prime number
range of the value
code finished'''


#AssertStatement

'''a=20
assert a<=10,'Invalid Number'

assert a>=10, 'valid Number'''


#customeException

'''class Balance(Exception):
    def __init__(self,args):
        self.msg=args
def checkbal():
    money=10000
    withdraw=9000
    try:
        balance=money-withdraw
        if(balance<=1000):
            raise Balance("insufficient balance")
        print(balance)
    except Balance as be:
        print(be)
checkbal()

output:

insufficient balance'''

       
#ExceptMultiple

'''a=10
b=0
try:
    d=a/b
    print(d)
except(NameError,ZeroDivisionError) as obj:
    print(obj)
print("rest of the code")

output:
division by zero
rest of the code'''

#TryExcept

'''a=10
b=0
try:
    d=a/b
    print(d)
    print("inside try")
except ZeroDivisionError:
    print("division by zero not allowed")
print("rest of the code")

output:

division by zero not allowed
rest of the code'''

#TryExceptElseFinally


'''a=10
b=0
try:
    d=a/b
    print(d)
    print("inside try")
except ZeroDivisionError:
    print("division error not allowed")
else:
    print("inside else")
finally:
    print("inside finally")
print("rest the code")

output:

division error not allowed
inside finally
rest the code'''


'''a=10
b=9
try:
    d=a/b
    print(d)
    print("inside try")
except ZeroDivisionError:
    print("division error not allowed")
else:
    print("inside else")
finally:
    print("inside finally")
print("rest the code")

output:

1.1111111111111112
inside try
inside else
inside finally
rest the code'''

#ExceptMultiple

'''a=10
b=0
try:
    d=a/b
    print(d)
except ZeroDivisionError as obj:
    print(obj)
except NameError as ob:
    print(ob)
print("rest of the code")

output:

division by zero
rest of the code
'''

'''a=10
b=2
try:
    d=a/b
    print(d)
except ZeroDivisionError as c:
    print(c)
except NameError as o:
    print(o)
print("rest of the code")


output:

5.0
rest of the code
'''
    

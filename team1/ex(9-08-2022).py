##1. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python. 
##

'''def fun(a):
    def fun1():
        return "<b>" + a()+"</b>"
    return fun1
def fun2(a):
    def fun1():
        return "<i>" +a()+"</i>"
    return fun1
def fun3(a):
    def fun1():
        return "<u>" +a()+"</u>"
    return fun1
@fun
@fun2
@fun3
def fun4():
    return "kavya bonnam"
print(fun4())
    
        
output:
<b><i><u>kavya bonnam</u></i></b>
'''

##2. Write a Python program to extract specified size of strings from a give list of string values using lambda.
##Original list:
##['Python', 'list', 'exercises', 'practice', 'solution']
##length of the string to extract:
##8
##After extracting strings of specified length from the said list:
##['practice', 'solution']

'''l=["python","list","exercises","practice","solution"]
l1=list(filter(lambda x:len(x)==8,l))
print(l1)

output:

['practice', 'solution']'''


##3. Write a Python program to create a deep copy of a given dictionary. Use copy.copy
'''import copy
l={1:"priya",2:"vicky",3:"picky"}
l2=copy.deepcopy(l)
print(l2)

output:
 {1: 'priya', 2: 'vicky', 3: 'picky'}'''

##4. Write a Python Program to Check a Number is a Spy Number or Not? note:- without  forloop.

'''num=int(input("enter a number"))
sum=0
product=1
num1=num
while(num>0):
    d=num%10
    sum=sum+d
    product=product*d
    num=num//10
if(sum==product):
    print("{} is a spy number!".format(num1))
else:
    print("{} is not a spy number".format(num1))
    
output:

enter a number45
45 is not a spy number

enter a number2
2 is a spy number!'''
        

##5. Write a Python program to find the XOR of two given strings interpreted as binary numbers.
##Input:
##['0001', '1011']
##Output:
##0b1010
##Input:
##['100011101100001', '100101100101110']
##Output:
##0b110001001111

'''n=['0001','1011']
c=int(n[0],2)^int(n[1],2)
print(c)
print(bin(c))
n=['100011101100001','100101100101110']
d=int(n[0],2)^int(n[1],2)
print(bin(d))

output:
10
0b1010
0b110001001111'''

    

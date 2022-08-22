##1write a program to print the list of elements of prinicipal diaognal
##input:
##3 3
##1  2 3
##10 20 30
##5  10 15
##output:[1, 20, 15]
'''def prinicipal_diagonal(matrix):
    list1=[]
    c=0
    for i in matrix:
        if c<b:
            list1+=[i[c]]
            c=c+1
    print(list1)
def conv_str_to_int(lista):
    list2=[]
    for i in lista:
        list2+=[int(i)]
    return list2
a,b=input().split()
a,b=int(a),int(b)
numlist=[]
for i in range(a):
    lista=input().split()
    lista=conv_str_to_int(lista)
    numlist+=[lista]
prinicipal_diagonal(numlist)'''

##2.wap take a string sparate with space and done add,sub,mul,div?
##eg:- input:-18 7
##     output:-(25,12,126,2)



'''def fun(a,b):
    print("add",a+b)
    print("sub",a-b)
    print("mul",a*b)
    print("div",a//b)
fun(18,7)'''

'''class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
         return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a//self.b
c=A(18,7)
d=c.add()
e=c.sub()
f=c.mul()
g=c.div()
list=[d,e,f,g]
print(tuple(list))'''


##3.In this question, we will provide an integer int_1, we have already declared the calculate_sum 
##function for you in solution.py. The initial int_1 of this function represents the initial value, 
##and you need to calculate the form a + aa + aaa + aaaa value, and finally print the result.
##input:5
##output:6170
##        


'''a=int(input("enter a value:"))
b=0
c=0
for i in range(1,a):
    b=b*10+a
    c=c+b
print(c)'''



##4.Please complete the code in solution.py to realize the function of get_sum. get_sum function receives an array parameter nums. Please use the lambda function to pass 
##in two unknown number x and y for the get_sum function and take this lambda function as the return value of the get_sum function. For the parameter nums received by get_sum, 
##if the length of the array num is an even number, return the sum of nums by x times. If the length of the array num is an odd number, return the sum of nums by -y times.
##input:[1,2,3,4]
##       2,3
##output:20

'''a=[1,2,3,4]
sum=0
for i in a:
    sum=sum+i
print(sum)
if sum%2==0:
    sum=sum*2
    print("the sum of even values:",sum)
else:
    sum=sum-1
    print("the sum of odd values",sum)'''


## 5.Mathematicians have come up with a famous conjecture - the Collatz conjecture.
##For any positive integer n, if n is even, make it n // 2.
##If n is an odd number, make it 3 * n + 1.
##If you follow this rule, you must end up with 1.
##How many rounds of transformation will that number go through to become 1?


##def collatz(n):
##    while n > 1:
##        print(n, end=' ')
##        if (n % 2):
##            # n is odd
##            n = 3*n + 1
##        else:
##            # n is even
##            n = n//2
##    print(1, end='')
## 
## 
##n = int(input('Enter n: '))
##print('Sequence: ', end='')
##collatz(n)
##



'''n=int(input(""))
while n>1:
    if n%2==0:
        n=n//2
        print(n)
    else:
        n=3*n+1
        print(n)'''

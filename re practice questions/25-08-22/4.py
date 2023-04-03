##16.write a program Example 9: Pascal's Triangle
##           1
##         1   1
##       1   2   1
##     1   3   3    1
##   1  4    6   4   1
## 1  5   10   10  5   1

'''from math import factorial
n=5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
    print()

output:

      1 
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6 4 1 

'''

##17.write a program to count number of chareters and print accending and desending order
##input:RameshRam
##output:a-2,e-1,h-1,m-2,R-2,s-1- assending
##decending :s-1,R-2m-2,,h-1,e-1a-2,

'''a="priyakota"
b=[]
count=0
for i in a:
    b.append(i)
c=set(b)
for i in c:
    x=a.count(i)
    print(i,x)
y=set(b)
print(c)
for j in c:
    y=a.count(i)
i=sorted(list(c))
print(i)
h=i[::-1]
print(h)

output:

p 1
t 1
i 1
a 2
o 1
k 1
y 1
r 1
{'p', 't', 'i', 'a', 'o', 'k', 'y', 'r'}
['a', 'i', 'k', 'o', 'p', 'r', 't', 'y']
['y', 't', 'r', 'p', 'o', 'k', 'i', 'a']
'''
##18.Python Program to Find HCF or GCD
'''a=int(input("enter a number:"))
b=int(input("enter a number:"))
if a>b:
    smaller=a
else:
    smaller=b
for i in range(1,smaller+1):
    if((a%i==0)and(b%i==0)):
        hcf=i
print("the hcf result is:",hcf)


output:

enter a number:2
enter a number:3
the hcf result is: 1

'''
##19.#Write a Python program to find the list with maximum and minimum length using lambda.

'''l=[1,2,3,4,5,6,8,0,678]
print(max(l,key=lambda value:int(value)))
print(min(l,key=lambda value:int(value)))

a=[1,2,3,4,5,6,7]
b=lambda x:min(x)
c=lambda x:max(x)
print(b(a))
print(c(a))
output:
678
0
'''


##20.Write a Python program to count the same pair in two given lists. use map() function.

'''from operator import eq
l=[1,2,7,4,5,10]
l2=[6,1,7,4,8,9,10]
a=sum(map(eq,l,l2))
print(a)

output:

2'''


'''from operator import eq
def fun(l,l2):
    a=sum(map(eq,l,l2))
    return a
l=[1,2,3,4,5]
l2=[1,0,3,5,6,7]
print("original lists")
print(l)
print(l2)
print("after counting the list")
print(fun(l,l2))

output:

original lists
[1, 2, 3, 4, 5]
[1, 0, 3, 5, 6, 7]
after counting the list
2
'''

##
##def computeGCD(x, y):
## 
##   while(y):
##       x, y = y, x%y
##       return abs(x)
## 
##a = 60
##b = 48
## 
### prints 12
##print ("The gcd of 60 and 48 is : ",end="")
##print (computeGCD(60, 48))



x=60
y=48
x,y=y,x%y
print(abs(x))


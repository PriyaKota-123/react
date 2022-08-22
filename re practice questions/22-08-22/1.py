##1)wap to print range of twin prime numbers by not using function

'''for i in range(2,20):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        x=i+2
        for k in range(2,x):
            if x%k==0:
                break
        else:
          print(i,x)
        
output:
3 5
5 7
11 13
17 19'''


##2) wap to print perimutations of the string "abc" by not using function.

'''from itertools import permutations
import string
s="abc"
a=string.ascii_letters
p=permutations(s)
d=[]
for i in list(p):
    if(i not in d):
        d.append(i)
        print("".join(i))
output:
abc
acb
bac
bca
cab
cba
'''
from itertools import permutations
import string
s="abc"
a=string.ascii_letters
p=permutations(s)
d=[]
for i in list(p):
    if(i not in d):
        d.append(i)
        print("".join(i))

##3) wap to print even and odd numbers separatly from a list by using filter function.

'''a=[1,2,3,4,5,6,7,8,9,10]
b=list(filter(lambda x: x%2==0,a))
print(b)

output:

[2, 4, 6, 8, 10]'''


'''a=[1,2,3,4,5,6,7,8,9,10]
b=list(filter(lambda x:x%2!=0,a))
print(b)

output:

[1, 3, 5, 7, 9]
'''


##4) wap to print range of fibonacci series by using recursion function.

'''a=0
b=1
print(a)
print(b)
for i in range(20):
    c=a+b
    a=b
    b=c
    print(c)
output:
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946'''

##def fib(n):
##    if n<=1:
##        return n
##    else:
##        return fib(n-1)+fib(n-2)
##a=int(input())
##for i in range(a):
##    print(fib(i))

'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
a=int(input())
for i in range(a):
    print(fib(i))

output:
9
0
1
1
2
3
5
8
13
21'''

##5) wap to print the strings from a list which are having the length of the list.
##
'''s=input().split()
print(len(s))

output:
priya how are u

4
 '''

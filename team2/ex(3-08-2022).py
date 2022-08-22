##1. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.

'''def str(a):
    while '01' in a:
        a=a.replace('01','')
    return len(a)==0
a="01010101"
print("original str",a)
print("check whether it is true or false")
print(str(a))
a="00"
print(str(a))
a="000111000111"
print(str(a))
a="00011100011"
print(str(a))

output:

original str 01010101
check whether it is true or false
True
False
True
False'''



##2. Write a Python program to add more number of elements to a deque object from an iterable object.

'''import collections
a=(2,4,6,8,9)
b=collections.deque(a)
print("numbers")
print(b)
c=(10,11,12,13,14)
b.extend(c)
print("added numbers")
print(b)

output:
numbers
deque([2, 4, 6, 8, 9])
added numbers
deque([2, 4, 6, 8, 9, 10, 11, 12, 13, 14])'''


##3.Reverse a list without using inbuit method and [::-1]

'''def r(l):
    r1=[]
    for i in l:
        r1.insert(0,i)
    return r1
l=[1,2,3,4,5]
print(r(l))

input:
l=[1,2,3,4,5]
output:
l=[5,4,3,2,1]'''


##4.cummulative sum of a list

'''def cummulative(list):
    a=[]
    b=len(list)
    a=[sum(list[0:x:1]) for x in range(0,b+1)]
    return a[1:]
list=[10,20,30,40,50]
print(cummulative(list))

output:
[10, 30, 60, 100, 150]'''



##5.write one example for pickling and unpickling?

##import pickle
##def pick():
##    a=[]
##    f=open("data.txt","ab")
##    pickle.dump(a,f)
##    
##pick()


import pickle
def pick():
    f=open("data.txt","rb")
    pickle.load(f)
pick()                                                                                                                                                                                                                                     
    


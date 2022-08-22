##1.write a python program on logging

'''from logging import *
basicConfig(filename="logfile110.log",filemode="w",level=INFO,format='%(lineno)s,%(asctime)s,%(message)s')
debug("this is debug")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")

output:

6,2022-08-11 12:03:00,681,this is info
7,2022-08-11 12:03:00,682,this is warning
8,2022-08-11 12:03:00,682,this is error
9,2022-08-11 12:03:00,682,this is critical'''
    

##2.write a python program to remove all the occurances of the given number

'''l=[1,2,3,5,4,5,6,7]
a=int(input("enter: "))
x=l.count(a)
for i in range(x):
    l.remove(a)
print(l)

output:

enter: 5
[1, 2, 3, 4, 6, 7]'''
    

##3.write a python program to exact the numbers in a given string and print sum,minimum and maximum of those numbers

'''l=input("enter a number")
a=[]
for i in l:
   if i.isdigit():
       a.append(int(i))
print(sum(a))
print(min(a))
print(max(a))


output:

enter a numberpriya456m
15
4
6'''
    
##4.write a python program on sprial number 
##eg:-9 8 7     
##    2 1 6        
##    3 4 5

'''n = 1
order = [0,1,2,5,8,7,6,3,4]
lst = [1,2,3,4,5,6,7,8,9]
for i in order:
    lst[i]=n
    n+=1
print(lst)

m = 0
for i in lst:
    print(i,end=" ")
    m+=1
    if m%3==0:
        print()

output:

[1, 2, 3, 8, 9, 4, 7, 6, 5]
1 2 3 
8 9 4 
7 6 5 
'''    

##5.create a list of combinations of entered number like below
##input: 5
##list must be created as [4,4,4,33,33,22,22,1,1,1]

'''a=int(input())
b=[]
for i in range(a-1,0,-1):
    if i==1 or i==a-1:
        b.append(i)
        b.append(i)
        b.append(i)
    else:
        b.append(str(i)*2)
        b.append(str(i)*2)
print(b)


output:

5
[4, 4, 4, '33', '33', '22', '22', 1, 1, 1]'''
    

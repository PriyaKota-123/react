##1.write a python program in shutil module using copy method

















##2.write a pthon program in os module using rename method

import os
s="usha sindhura"
r="priya kota"
os.rename(s,r)
print("sucessfully")







##3.write a python program in fibonacci series using outer and inner functions


'''def fun(a):
    def fun1():
        #n=int(input("enter a nuumber"))
        a=0
        b=1
        print(a)
        print(b)
        for i in range(1,10):
            c=a+b
            a=b
            b=c
            print(c)
    return fun1
def fun2():
    pass
r=fun(fun2())
r()'''




##4.write a python program in heapq module
##5.write a python program in shallow copy and deep copy

#deep copy
'''import copy
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=copy.deepcopy(l1)
print("old list",l1)
print("new list",l2)
'''
#shallow copy

'''import copy
l=[1,2,3,4,5,6,7,8]
l2=copy.copy(l)
print("old list",l)
print("new list",l2)'''


'''l=[1,2,3,4,"a"]
l2=l
l2[4]=5
print(l)
print(l2)'''



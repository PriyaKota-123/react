##1.write a program to count elements in a file?
'''f=open("text.txt","r")
d=f.read()
count=0
for i in d:
    count=count+1
    print(count)
f.close()
'''    


##2.write a python program on atleast three magic methods?

#add
'''class emp:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b
e=emp(3)
print(e+6)'''
        

#abs

'''class emp:
    pass
    def  __abs__(self,a):
        self.a=a
        print(self.a.__abs__())
e=emp()
e.__abs__(-20.5)'''


#iadd
'''
class emp:
    def __init__(self,a):
        self.a=a
    def __iadd__(self,b):
        return self.a+b
num=5
num+=7
print(num)

x1=10
x2=20
print(x1+x2)
        
print(x1.__add__(x2))
'''
##3.Write python program on multithreading?

'''from threading import Thread
def disp(a,b):
    print("",a)
    print("",b)
t=Thread(target=disp,args=(10,20))
t.start()'''



##4.Write a dictionary to a file in Python

f=open("text1.txt","r")
d=f.read()
print(d)






##5.write the program to Get Yesterday’s date using Python?

'''from datetime import date
from datetime import timedelta
today=date.today()
print(today)
yesterday=today-timedelta(days=1)
print(yesterday)

output:
2022-08-06
2022-08-05
    '''

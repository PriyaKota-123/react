##1) create a nested list by taking list elements from the user like below
##[1,2,[3,4],[5,6,7],8,9]'''
'''n = int(input('enter the no.of elements in a list: '))
lst= []

for i in range(n):
    m = input()
    if ' ' in m:
        lst2 = []
        for i in m.split():
            lst2.append(int(i))
        lst.append(lst2)
        
    else:
        lst.append(int(m))

print(lst)'''

##2) write a program on to retrieve the data from the file and use seek() and tell() method'

'''with open('data.txt', 'w') as f:
    f.write('write a program on rlock in multithreading\nwap to create three functions and three threads\nfor each functions and run those threads')
    
with open('data.txt', 'r') as f:
    for i in range(3):
        print(f.readline())
        f.seek(20)
        print(f.tell())'''


    
#3) write a program on rlock in multithreading'
'''from threading import *

class Multi:
    def __init__(self, balance):
        self.balance = balance
        self.l = RLock()

    def disp(self):
        name = current_thread().name
        self.l.acquire()
        for i in range(2):
            print(f'this is {name} thread running 2 times')
        
        self.l.acquire()
        self.l.release()
        self.l.release()
        
        for j in range(2):
            print('another for loop for {name}')
        
obj = Multi(300)
t1 = Thread(target=obj.disp, name = 'first thread')
t2 = Thread(target=obj.disp, name = 'second thread')
t1.start()
t2.start()
t1.join()
t2.join()'''
        


##4) wap to create three functions and three threads for each functions and run those threads'
'''from threading import Thread

def fun1():
    print('this is first function')
    
def fun2():
    print('this is second function')
    
def fun3():
    print('this is third function')

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t3 = Thread(target=fun3)
t1.start()
t2.start()
t3.start()


for i in [fun1,fun2,fun3]:
    t = Thread(target=i)
    t.start()
    t.join()'''


##5) wap to print the next 100th decimal of entered user input 
##input = 129, output = 200 , if input = 334, output=400'''

'''n = int(input("entera anumber"))

m = 100

while m<n:
    m += 100
print(m)'''



























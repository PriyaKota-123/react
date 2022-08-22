#creating a thread by creating a child class to thread class

'''from threading import Thread
class mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("child thread ")
    def m1(self):
        pass
t=mythread()
t.start()
print("main thread")

output:

child thread 
main thread'''


#creating a thread by creating a child class to thread class by passing arguments

'''from threading import Thread
class mythread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("thread constructor",a)
    def m1(self):
        pass
t=mythread(22)
t.start()
print("main thread")

output:
thread constructor 22
main thread'''


#creating a thread without creating a child class to thread class

'''from threading import Thread
class mythread:
    def disp(self,a,b):
        print(a,b)
m=mythread()
t=Thread(target=m.disp,args=(10,20))
t.start()


 output:

 10 20
'''


#single tasking using thread

'''from threading import Thread
from time import *
class myexam:
    def s(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print("task1 completed")
    def task2(self):
        print("task2 completed")
    def task3(self):
        print("task3 completed")
m=myexam()
t=Thread(target=m.s)
t.start()

output:

task1 completed
task2 completed
task3 completed'''


# Multitasking using Multiple Thread
# Two task using Two Threads
'''from threading import Thread
class h:
    def __init__(self,t):
        self.t=t
    def food(self):
        for i in range(1,6):
            print(self.t,i)
h1=h("take order from table")
h2=h("serve order to table")
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
t2.start()


output:

take order from tableserve order to table  11

take order from tableserve order to table  22

take order from tableserve order to table  33

take order from tableserve order to table  44

take order from tableserve order to table  55'''



#multitasking using multiple thread using LOCK
#two threads acting on same method
'''from threading import *
class flight:
    def __init__(self,avail_seat):
        self.avail_seat=avail_seat
        self.l=Lock()
    def reserve(self,need_seat):
            self.l.acquire(blocking=True)
            print("available seats",self.avail_seat)
            if(self.avail_seat >= need_seat):
                name=current_thread().name
                print(f"{self.avail_seat} seat is alloted for {name}")
                self.avail_seat -= need_seat
            else:
               print("sorry all seats are alloted")
            self.l.release()

            
f=flight(3)
t1=Thread(target=f.reserve,args=(1,),name="rahul")
t2=Thread(target=f.reserve,args=(1,),name="sonam")
t3=Thread(target=f.reserve,args=(1,),name="vicky")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("main thread")


output:

available seats
available seats  11

1 seat is alloted for rahul1 seat is alloted for sonam

available seats 3
3 seat is alloted for rahul
available seats 2
2 seat is alloted for sonam
available seats 1
1 seat is alloted for vicky
main thread
'''

#multitasking using multiple thread using RLOCK
#two threads acting on same method

'''from threading import *
class flight:
    def __init__(self,avail_seat):
        self.avail_seat=avail_seat
        self.l=RLock()
    def reserve(self,need_seat):
            self.l.acquire()
            self.l.acquire()
            print(self.l)
            print("available seats",self.avail_seat)
            if(self.avail_seat >= need_seat):
                 name=current_thread().name
                 print(f"{self.avail_seat} seat is alloted for {name}")
                 self.avail_seat -= need_seat
            else:
                print("sorry all seats are alloted")
            self.l.release()
            self.l.release()
f=flight(8)
t1=Thread(target=f.reserve,args=(1,),name="rahul")
t2=Thread(target=f.reserve,args=(1,),name="sonam")
t3=Thread(target=f.reserve,args=(1,),name="vicku")
t1.start()
t2.start()
t3.start()
##t1.join()
##t2.join()
##t3.join()
print("main thrad")

output:

<locked _thread.RLock object owner=10616 count=2 at 0x000001269CD95F80>
available seats 8
8 seat is alloted for rahul
<locked _thread.RLock object owner=6848 count=2 at 0x000001269CD95F80>
available seats 7
7 seat is alloted for sonam
<locked _thread.RLock object owner=13384 count=2 at 0x000001269CD95F80>
available seats 6
6 seat is alloted for vicku
main thrad'''



# Multitasking using Multiple Thread using SEMAPHORES
# Two Threads acting on same method

'''from threading import *
class Flight:
	def __init__(self, available_seat):
		self.available_seat = available_seat
		self.l = BoundedSemaphore(3)
		print(self.l)
		
	def reserve(self, need_seat):
		self.l.acquire()
		print(self.l._value)
		print('Available Seats:', self.available_seat)
		if(self.available_seat >= need_seat):
			name = current_thread().name
			print(f'{need_seat} seat is alloted for {name}')
			self.available_seat -= need_seat
		else:
			print('Sorry! All seats has alloted')
		self.l.release()
f = Flight(5)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")

output:

<threading.BoundedSemaphore object at 0x000001C02C1AE200>
210
Available Seats:Available Seats:Available Seats:   555
1 seat is alloted for Rahul1 seat is alloted for Sonam1 seat is alloted for Raj
Main Thread'''

# DeadLock

'''from threading import *
l1 = Lock()
l2 = Lock()

def bookticket():
	l1.acquire()
	print('Bookticket Locked on plan')
	print('Bookticket wants to lock Class')
	l2.acquire()
	print('Bookingticket locked seat')
	l2.release()
	l1.release()
	print('Booking ticket done')
	
def cancelticket():
	l2.acquire()
	print('cancelticket Locked on Class')
	print('cancelticket wants to lock Plan')
	l1.acquire()
	print('cancelingticket locked seat')
	l1.release()
	l2.release()
	print('canceling ticket done')	
	
t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)
t1.start()
t2.start()

output:

Bookticket Locked on plancancelticket Locked on Class

Bookticket wants to lock Classcancelticket wants to lock Plan'''









##from threading import Thread
##class my(Thread):
##    def __init__(self,a):
##        Thread.__init__(self)
##        print("child ",a)
##    def main(self):
##        pass
##t=my(29)
##t.start()
##print("main thread")


##from threading import Thread
##class name:
##    def my(self,a,b):
##        print(a,b)
##m=name()
##m1=Thread(target=m.my,args=(12,34))
##m1.start()
##


##from threading import Thread
##from time import *
##class myexam:
##    def s(self):
##        self.task1()
##        self.task2()
##        self.task3()
##    def task1(self):
##        print("task1 completed")
##    def task2(self):
##        print("task2 completed")
##    def task3(self):
##        print("task3 completed")
##m=myexam()
##t=Thread(target=m.s,args=())
##t.start()

##
##from threading import Thread
##class h:
##    def __init__(self,t):
##        self.t=t
##    def food(self):
##        for i in range(1,6):
##            print(self.t,i)
##h1=h("take order")
##h2=h("serve the order")
##t1=Thread(target=h1.food)
##t2=Thread(target=h2.food)
##t1.start()
##t2.start()



'''from threading import *
class d:
    def __init__(self,a):
        self.a=a
        self.l=Lock()
    def s(self,need):
        self.l.acquire(blocking=True)
        if(self.a>=need):
            name=current_thread().name
            print(f"{self.a} seat is alloted for {name}")
            self.a-=need
        else:
            print("sorry")
        self.l.release()
D=d(3)
t1=Thread(target=D.s,args=(1,),name="priya")
t2=Thread(target=D.s,args=(1,),name="vicky")
t3=Thread(target=D.s,args=(1,),name="picky")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("main thread")
'''

'''from threading import *
l1=Lock()
l2=Lock()
def book():
    l1.acquire()
    print("book locked on plan")
    print("want to lock class")
    l2.acquire()
    print("locked seat")
    l2.release()
    l1.release()
    print("booking tickett done")
    
def cancel():
    l2.acquire()
    print("cancel")
    print("wants to lock plan")
    l2.acquire()
    print("locked seat")
    l1.release()
    l2.release()
    print("ticket done")
t1=Thread(target=book)
t2=Thread(target=book)
t1.start()
t2.start()'''




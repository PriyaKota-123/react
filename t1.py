#1.WAP take one example duck typing,in this methods you must take 3 defferent classes names and in each one class you must take 3 different methods.

'''class Rabbit():
    def walk(self):
        print("TATATATST")
    def eat(self):
        print("rabbit eat carrot")
    def sleep(self):
        print("rabbit sleep on grass")
class parrots():
    def walk(self):
        print("TATATATST")
    def eat(self):
        print("parrot eat fruits")
    def sleep(self):
        print("parrot sleep on tree")
class peacock():
    def walk(self):
        print("dadadsfad")
    def eat(self):
        print("eating grass")
    def sleep(self):
        print("sleep on grass")
obj=Rabbit()
obj1=parrots()
obj2=peacock()
for A in (obj,obj1,obj2):
    A.walk()
    A.eat()
    A.sleep()'''


#2.WAP take one example wrong method overloading.
'''class girl():
     def rose(self,a):
        print("rose flower")
     def rose(self):
        print("rose flower is beautiful")
obj=girl()
obj.rose()
obj.rose(4)'''


'''class A:
    def sum(self,a):
        print("1st sum method",a)
    def sum(self):
        print("2nd sum method")
s=A()
s.sum()
s.sum(10)'''



##3). wap solve this pattern
##
##  5 5 5 5 5
##   * * * *
##    3 3 3 
##     * *
##      1

'''n=6
for x in range(1,n+1):
    print(" "*x,end=" ")
    for y in range(n-x):
        if x%2==0:
                print("*",end=" ")
        else:
            print(n-x,end=" ")
    print()'''
n=6
for i in range(1,n+1):
    print(" "*i,end=" ")
    for j in range(n-i):
        if i%2==0:
            print("*",end=" ")
        else:
            print(n-i,end=" ")
    print()
#4.WAP take one example of hierarchical method.
'''class father():
    def show(self):
        print("father method")
class son(father):
    def show1(self):
        print("son method")
class daughter(father):
    def show2(self):
        print("daughter method")
d=daughter()
d.show()
d.show2()
s=son()
s.show()
s.show1()'''

#5). What is the difference between Python Arrays and lists take one eaxmple ?


'''list=[1,"priya",['a','e']]
print(list)


import array
s=array.array('i',[1,3,4])
print(s)'''

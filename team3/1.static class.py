##1.WAP to call parent class static static method from child class static method.

'''class Teacher(object):

    @staticmethod
    def show():
        print("Parent Class Static Method")

class Student(Teacher):
    @staticmethod
    def display():
        Teacher.show()
        

a=Student()
a.display()'''




##2.write demo programs for method overriding,constructor overriding,program with variable number of arguments.

 #Constructor Overriding with Parameter

'''class Father:					# Parent Class
	def __init__(self, m):
		self.money = m
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method")
		
		
class Son(Father):				# Child Class
	def __init__(self, r):
		self.money = r
		self.car = 'BMW'
		print("Son Class Constructor")
		
	def disp(self):
		print("Son Class Instance Method")

s = Son(2000)
print(s.money)
print(s.car)
s.disp()
s.show()'''




####4.wap that take a two two strings from input and return the combination of the two string characters like below:
##input:
##string1="harry"
##string2="micheal"
##output:
##['hm','ai','rc','rh','ae','ya','l']
##

'''s1=input("Enter a String:")
s2=input("Enter a String:")
output=""
i=0
j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output+=s1[i]
        i=i+1
    if j<len(s2):
        output+=s2[j]+","
        j=j+1
print(output)'''





##5.wap to take a list and sort the list not using the sorted or sort() method
##input:  [2,5,12,6,1,4]
##output:   [1,2,4,5,6,12]
##and not using max() or min() method'''

'''data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print (new_list)



l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print (l)'''


##3.create one object for child class and using that object print both constructor print statemts from parent classes.
'''class Father:
    def __init__(self):
        print("Father Class Instance Method")
class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son class Instance Method")

s=Son()'''















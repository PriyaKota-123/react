##1.Write a Python class to get all possible unique subsets from a set of distinct integers.
##Input : [4, 5, 6]
##Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

'''from itertools import *
class A:
    def __init__(self,a):
        self.a=a
    def show(self):
        print("combinations",self.a)
a=A(4,5,6)
a.show()
print(list(combinations(4,a)))
print(list(combinations(5,a)))
print(list(combinations(6,a)))'''


##2.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
##Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
##Output : [[-10, 2, 8], [-7, -3, 10]]




##3.Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

'''class A:
    def __init__(self):
        pass
    def get_string(self,a):
        self.a=int(input(""))
class B(A):
    def __init__(self):
     super.__init__(a)
    def print_string(self,b):
        self.b=b
b=B()
c=b.print_string()
print(c.uppercase())
a=A()
print(a.get_string())'''


    




##4.Write a Python program to count the frequency of words in a file

f=open("data.txt","r")
d=f.readlines()
d=d.split()
count=0
for i in d:
    count=count+i
    print(count)
f.close()
    

##5.Write a Python program to extract characters from various text files and puts them into a list.

#6.Write a Python program to generate the running product of the elements of an given iterable.

##7.A class Student is given to you. Add details in the Student class. 
##Student: 
##Instance Variables: studentId : PUBLIC  , studentName : PUBLIC , 
##Marks: PRIVATE, grade: PRIVATE 
##PUBLIC Methods: displayDetails(): , 
##PRIVATE METHOD : calculateGrade():
##Default constructor 
#A constructor that that takes the following parameter: studentId, studentName, marks. 
#Note that grade is not set either through constructor or setter as it is a calculated value. 
 
#Methods 
#displayDetails(): This method should display the details of the student in the following format: 
#Student [name=John Smith, studentId=123, marks=95, grade=A] 
 
#calculateGrade(): This is a private method that calculates the grade based on the marks that is set. If marks is above 90, grade is set to A. If marks is between 80 and 90, grade is set to B, if marks is between 70-80 grade is set to C, if marks is between 60-70, grade is set to D, if marks is less than 60, grade is set to E.Use this method when you need to set or reset grade


##8.In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year), separated by comma / space or both and return the date in the format of YYYY-MM-DD. 
##Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012 
##Output : 2012-05-21 
## 
##Note the following: 
##The input can have comma, space or both. No other separator is allowed 
##The month can be given in full form (January, February etc) or in short 3-Letter form (Jan, feb,mar, apr, may, jun, jul, aug, sep, oct, nov, dec) . This program should accept both types. 
##Output month should always be a number. 
##Validate for invalid values. 
##Return null for error in input.

##9.Write a python program on filtering consonants 
## 
##Note the following points: 
##The method should scan the given input, remove all the consonants and return the resulting string. 
##The output should contain only vowels and all other characters, including special characters should be filtered out. 
##If input is null, return null. 
##Example input: “Telephone”, Output: “eeoe” 

##10.Write a python program to find factorial , Fibonacci series, sum of digits, product of digits, reverse of a number, amstrong number.

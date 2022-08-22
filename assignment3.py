'''1. 4.Write a Python class to get all possible unique subsets from a set of distinct integers.

Input : [4, 5, 6]

Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''
##from itertools import combinations
##lst = [4,5,6]
##lst2 = []
##for i in range(len(lst)+1):
##    n = list(combinations(lst,i))
##    for j in n:
##        lst2.append(list(j))
##print(lst2)


'''2. Write a Python class to find the three elements that sum to zero from a set of n real numbers.

Input array : [-25, -10, -7, -3, 2, 4, 8, 10]

Output : [[-10, 2, 8], [-7, -3, 10]]'''

##from itertools import combinations
##lst = [-25,-10,-7,-3,2,4,8,10]
##lst2 = []
##for i in range(len(lst)+1):
##    n = list(combinations(lst,3))
##    for j in n:
##        if sum(j)==0 and list(j) not in lst2:
##            lst2.append(list(j))
##print(lst2)


'''3. Write a Python class which has two methods get_String and print_String. get_String accept a string
from the user and print_String print the string in upper case'''
##class String:
##    
##    def get_String(self,name):
##        self.name = name
##    
##    def print_String(self):
##        print(self.name.upper())
##
##name = input('>: ')
##obj = String()
##obj.get_String(name)
##obj.print_String()


'4. Write a Python program to count the frequency of words in a file'

##import collections
##with open('data.txt','r') as f:
##    r = f.read()
##    print(collections.Counter(r))



'5. .Write a Python program to extract characters from various text files and puts them into a list.'
##a = 'abcd'
##for i in a:
##    with open(i+'.txt','w') as f:
##        f.write(f"this is '{i}' page")
##
##lst = []
##char = 'aeiou'
##for i in a:
##    with open(i+'.txt','r') as f:
##        r = f.read()
##        for i in r:
##            if i in char:
##                lst.append(i)
##print(lst)


'6. Write a Python program to generate the running product of the elements of an given iterable.'
'using itertools'
##import itertools
##lst = [0,1,2,3,4,5,6]
##lst2 = []
##l = itertools.accumulate(lst)
##print(list(l))

'''output:
        [0, 1, 3, 6, 10, 15, 21]'''

'not using itertools'
##n = 0
##for i in range(len(lst)):
##    n = n+lst[i]
##    lst2.append(n)
##print(lst2)

'''output:
[0, 1, 3, 6, 10, 15, 21]
         '''



'''7. A class Student is given to you. Add details in the Student class.

Student:

Instance Variables: studentId : PUBLIC , studentName : PUBLIC ,

Marks: PRIVATE, grade: PRIVATE

PUBLIC Methods: displayDetails(): ,

PRIVATE METHOD : calculateGrade():

Default constructor

A constructor that that takes the following parameter: studentId, studentName, marks.

Note that grade is not set either through constructor or setter as it is a calculated value.

Methods

displayDetails(): This method should display the details of the student in the following format:
    
Student [name=John Smith, studentId=123, marks=95, grade=A]
f
calculateGrade(): This is a private method that calculates the grade based on the marks that is set. If marks is above 90, grade is set to A.
If marks is between 80 and 90, grade is set to B, if marks is between 70-80 grade is set to C, if marks is between 60-70, grade is set to D,
if marks is less than 60, grade is set to E.Use this method when you need to set or reset grade
f'''
##class Student:
##    __marks = 78
##    __grade = 'A'
##    
##    def __init__(self, std_id, std_name):
##        self.std_id = std_id
##        self.std_name = std_name
##        
##
##    def displayDetails(self):
##        return f'Student [name={self.std_name}, studentId = {self.std_id}, marks={self.__marks}, grade={self.__grade}]'
##
##    def __calculateGrade(self):
##        if self.__marks > 90:
##            self.__grade = 'A'
##
##        elif 90 > self.__marks >80:
##            self.__grade = 'B'
##
##        elif 80 >self.__marks> 70:
##            self.__grade = 'C'
##
##        elif 70 >self.__marks> 60:
##            self.__grade = 'D'
##
##        else:
##            self.__grade = 'E'
##
##        return self.__grade
##
##    def set_grade(self):
##        return self.__calculateGrade()
##            
##obj = Student(34,'ragin')
##print(obj.displayDetails())
##print(obj.set_grade())
##print(obj.displayDetails())


'''8. In the given Class DateFormatter, implement the method format() such that it accepts the date (date month year), separated by comma /
space or both and return the date in the format of YYYY-MM-DD.

Eg.: 21,May,2012 / 21 May 2012 / 21, May, 2012

Output : 2012-05-21

Note the following:

The input can have comma, space or both. No other separator is allowed

The month can be given in full form (January, February etc) or in short 3-Letter form (Jan, feb,mar, apr, may, jun, jul, aug, sep, oct, nov, dec) .
This program should accept both types.

Output month should always be a number.

Validate for invalid values.

Return null for error in input.'''
##import datetime
##a = input('>:')
##
##n = datetime.datetime.strptime(a,'%d,%B,%Y')
##n = datetime.datetime.strptime(a,'%d %B %Y')
##n = datetime.datetime.strptime(a,'%d, %B, %Y')
##
##print(n)


'''9. Write a python program on filtering consonants

Note the following points:

1. The method should scan the given input, remove all the consonants and return the resulting string.

2. The output should contain only vowels and all other characters, including special characters should be filtered out.

3. If input is null, return null.

4. Example input: “Telephone”, Output: “eeoe”'''
##def fil(s):
##    string = ''
##    for i in s:
##        if i in 'aeiou':
##            string += i
##    return string
##
##s = input('>:')
##print(fil(s))



'10. Write a python program to find factorial , Fibonacci series, sum of digits, product of digits, reverse of a number, amstrong number.'

'factorial'
##def outer(fun):
##    def inner(n):
##        fact = 1
##        for i in range(1,n+1):
##            fact = fact*i
##        fun(fact)
##    return inner
##
##@outer
##def fac(n):
##    print(n)
##
##fac(5)

'fibonacci'
##def outer(fun):
##    
##    def inner(n):
##        a = 0
##        b = 1
##        fun(n)
##        for i in range(n):
##            c = a+b
##            a = b
##            b = c
##            print(c)
##    return inner
##    
##@outer            
##def fib(n):
##    print('fibanocci series of given number is: ')
##
##fib(8)

'sum of digits'
##def outer(fun):
##    def inner(n,m):
##        fun(n,m)
##        d = n+m
##        print(d)
##    return inner
##
##@outer
##def sumof(n,m):
##    print('sum of two given digits are: ')
##
##sumof(2,5)

'product of numbers'
##def outer(fun):
##    def inner(n,m):
##        fun(n,m)
##        d = n*m
##        print(d)
##    return inner
##
##@outer
##def sumof(n,m):
##    print('product of two given digits are: ')
##
##sumof(2,5)

'reverse number'
##def outer(fun):
##    def inner(n):
##        fun(n)
##        s = str(n)
##        r = s[::-1]
##        print(int(r))
##        
##    return inner
##
##@outer
##def sumof(n):
##    print('reverse of a given number: ')
##
##sumof(2352)

'armstromg number'
##def outer(fun):
##    def inner(n):
##        count = 0
##        temp = n
##        while temp:
##            temp = temp//10
##            count += 1
##            
##        temp2 = n
##        count2 = 0
##        while temp2:
##            div = temp2%10
##            count2 = count2+(div**count)
##            temp2 = temp2//10
##        print(count2)
##        if count2 == n:
##            fun(n)
##        else:
##            print('it is not an armstrong number')
##        
##    return inner
##
##@outer
##def sumof(n):
##    print('it is a armstrong number')
##
##n = int(input(">: "))
##sumof(n)











        
        

























        
        








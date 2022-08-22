#1. Define a function that accepts roll number and returns whether the student is present or absent.

'''def student(a):
    b=int(input("enter a rollnumber"))
    if b in a:
        print("student present")
    else:
        print("student absent")
    
a=[203,204,205,206,207]
student(a)

#output:
enter a rollnumber204
student present'''

#===========================================================================
##2.a. Write a python program to print multiple arguments.
'''def multiple(*a):
    return a
print(multiple("priya","vicky","picky"))

#output:
('priya', 'vicky', 'picky')'''

##b. Write a function that accepts variable length key value pair as arguments

'''def show(**name):
    return name
print(show(a="priya",b="vicky",c="picky"))

#output:
{'a': 'priya', 'b': 'vicky', 'c': 'picky'}'''
#====================================================================================================
##3.a. Write a python program to find the power of a number using recursion

'''def fun(num,power,c):
     if power>1:
        num = num*c
        power -= 1
        fun(num,power,c)
     if power==1:
         print(num)
        
num = 12
power = 4
c = num
fun(num,power,c)

output:
    20736'''


'''def fun(num,power,c):
     if power>1:
        num = num*c
        power -= 1
        fun(num,power,c)
     if power==1:
         print(num)
        
num = 12
power = 4
c = num
fun(num,power,c)

output:
    20736'''

##b. Write a Python program of recursion list sum 
##Test Data: [1, 2, [3,4], [5,6]]
##Expected Result: 21

'''def sum(a):
    b=0
    for i in a:
        if type(i)==type([]):
            b=b+sum(i)
        else:
            b=b+i
    return b
a=[1,2,[3,4],[5,6]]
print(sum(a))

output:
21'''
 

#==========================================================================================================

##4. Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters, a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it

'''def outer(a,b):
    def inner():
        return a+b
    inner()
    return a+b+5
a=int(input("enter a number"))
b=int(input("enter a number"))
print(outer(a,b))

output
enter a number8
enter a number4
17'''

#=======================================================================================================

##5.a.  Assign a different name to function and call it through the new name


'''def name(a):
    print(a)
name("hello")
new_name="hi"
print(new_name)

#output:
hello
hi'''

##b.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000

'''def showEmployee(Empname="priya",Empsalary=9000):
    return Empname,Empsalary
print(showEmployee("priya"))


#output

('priya', 9000)'''
#=================================================================================================

##6.a. Write a Python function that takes a number as a parameter and check the number is prime or not. 

'''def prime(a):
    for i in range(2,a):
        if a%i==0:
            print("not a prime number")
            break
    else:
        print("it is prime number")
a=int(input("enter a number:"))
prime(a)
    

#output:
enter a number:9
not a prime number

enter a number:3
it is prime number'''

##b. Write a Python function that checks whether a passed number is palindrome or not. 

'''def palindrome(a):
    if a[::-1]:
        print(" it is a palindrome")
    else:
        print("not a plaindrome")
a=input("enter a number:")
palindrome(a)


#output:

enter a number:131
 it is a palindrome'''

#=======================================================================================================
##7.a. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
##


'''l=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("original list of tuple",l)
l.sort(key=lambda x: x[1])
print("after sorting the list of tuples",l)

###output:
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##after Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''



##b.Write a Python program to create Fibonacci series upto n using Lambda

'''from functools import reduce
fib=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fib(9))'''

'''from functools import reduce
fib=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fib(9))

#output:
[0, 1, 1, 2, 3, 5, 8, 13, 21]'''


##c.  Write a Python program to add two given lists using map and lambda.

'''a=[1,2,3,4]
b=[7,8,9,6]
add=list(map(lambda x,y:x+y,a,b))
print(add)

#output:
[8, 10, 12, 10]'''



('priya', 'vicky', 'picky')

##d. Write a Python program to find palindromes in a given list of strings using Lambda.  
##Orginal list of strings:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##List of palindromes:
##['php', 'aaa']

'''a=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print("original list of strings:",a)
x=list(filter(lambda x:(x==" ".join(reversed(x))),a))
print("list of palindrome:",x)

#output:
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']'''

##e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
##(Hint: lambda will be passed to sort method's key parameter as argument)

'''l=[1,2,3,6,4,8,9,5,1,100]
l.sort(key=lambda x:-x)
print(l)

#output:

[100, 9, 8, 6, 5, 4, 3, 2, 1, 1]'''


##f. Write a lambda function which takes z as a parameter and returns z*11

'''a=lambda z:z*11
print(a(10))

#output:
110'''


#==================================================================================================

##8.a. Using List Comprehension Find all of the numbers from 1–1000 that are divisible by 8
##
'''a=[i for i in range(1,1000) if i%8==0]
print(a)

#output:
[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952, 960, 968, 976, 984, 992]
'''


#b. Use list comprehension to contruct a new list but add 6 to each item.
'''l=[2,3,4,5]
l2=[i+6 for i in l]
print(l2)

#output:

[8, 9, 10, 11]'''


#===========================================================================================

##
##9. string = "Practice Problems to Drill List Comprehension in Your Head."
##Remove all of the vowels in a string (use string above)


'''l= "Practice Problems to Drill List Comprehension in Your Head."
for i in l:
    if i not in "aeiou":
        print(i,end="")

        
#output:
Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.'''

##Find all of the words in a string that are less than 5 letters (use string above)


'''string = "Practice Problems to Drill List Comprehension in Your Head."
lst2 = string.split(' ')
five = [i for i in lst2 if len(i)<5]
print(five)

#output:
    ['to', 'List', 'in', 'Your']'''


##Use a dictionary comprehension to count the length of each word in a sentence (use string above)

'''string = "Practice Problems to Drill List Comprehension in Your Head."
lst2 = string.split(' ')
dic = {i:len(i) for i in lst2}
print(dic)

output:
    {'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}'''

#============================================================================
##10. First, create a range from 100 to 160 with steps of 10.
##Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.


'''lst = [i for i in range(100,160,10)]

dic = {i:i%100 for i in lst}
print(dic)

#output:
    {100: 0, 110: 10, 120: 20, 130: 30, 140: 40, 150: 50}'''

'''l=[ i for i in range(100,160,10)]
dic={i:i%100 for i in l}
print(dic)

l=[i for i in range(100,160,10)]
dic={i:i%100 for i in l}
print(dic)'''
#=============================================================================

##11. Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with
##value above 2000 are taken to the new dictionary. dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}


'''dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}

dict2 = {i:dict1[i] for i in dict1 if dict1[i]>2000}
print(dict2)

output:
    {'NFLX': 4950, 'TREX': 2400}'''

'''dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={i:dict1[i] for i in dict1 if dict1[i]>2000}
print(dict2)

dict={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict1={i:dict[i] for i in dict if dict[i]>2000}
print(dict1)'''

#==============================================================================
#'12. Write a Python Set comprehension with an if clause example'
'''set1 = {i for i in range(1,10) if i%2==0}
print(set1)

output:
    {8, 2, 4, 6}'''


'''set1={i for i in range(1,10)if i%2==0}
print(set1)



set1={i for i in range(1,10)if i%2==0}
print(set1)'''

#==================================================================================




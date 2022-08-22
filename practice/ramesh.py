#1. Define a function that accepts roll number and returns whether the student is present or absent.

'''def attenndance(student_data):
    
    for key,value in present_students.items():
        #print(value)
        if n==int(value):
            print("Roll number",n,"is present")
            break
    else:
        print("Roll number",n,"is absent")

n = int(input("Enter Rollnumber"))
present_students={"suresh":2,"rakesh":3,"priya":4,"bhagavan":5}
student_data={"ramesh":1,"suresh":2,"rakesh":3,"priya":4,"bhagavan":5}
attenndance(student_data)'''


#output:
##Enter Rollnumber1
##Roll number 1 is absent
##
##Enter Rollnumber3
##Roll number 3 is present

##===================================================================================================================================================================

##2.a. Write a python program to print multiple arguments.

'''def multi_arguments(*a):
    return a

print(multi_arguments({"suresh":2,"rakesh":3},{"priya":4},{"bhagavan":5}))'''


##outpuit:
##({'suresh': 2, 'rakesh': 3}, {'priya': 4}, {'bhagavan': 5})

##===================================================================================================================================================================

##2 b. Write a function that accepts variable length key value pair as arguments.

'''def length_variable(a):
    for i in a:
        c.append(len(i))        
    #print(c)
    print(dict(zip(a,c)))
b={}
c=[]
a=["suresh","priya","ganeshaaa","lakkyboy"]
length_variable(a)'''

##output:
##    {'suresh': 6, 'priya': 5, 'ganeshaaa': 9, 'lakkyboy': 8}

##===================================================================================================================================================================

#3.a. Write a python program to find the power of a number using recursion

def power_of_number(a):
    return a**a
a =int(input("enter number"))
def power(power_of_number):
    return 
print(power_of_number(a))
##output
##enter number4
##256

##===================================================================================================================================================================
##b. Write a Python program of recursion list sum 
##Test Data: [1, 2, [3,4], [5,6]]
##Expected Result: 21

'''def list_sum(Test_data):
    sum=0
    for i in Test_data:
        if type(i)==type([]):
            sum+=list_sum(i)
        else:
            sum+=i
    return sum
Test_data=[1, 2, [3,4], [5,6]]
print(list_sum(Test_data))'''

##output:
##    21



##===================================================================================================================================================================
##
##4. Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters, a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it
##
##
'''
def out_function(a,b):
    def inner():
        return a+b
    inner()
    return a+b+5
a=int(input("enter a value"))
b=int(input("enter a value"))
print(out_function(a,b))'''
#output
##enter a value5
##enter a value9
##19


##===================================================================================================================================================================



#5.a.  Assign a different name to function and call it through the new name
#def diif():





##    
##b. 15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both,
##and if the salary is missing in function call it should show it as 9000

##===================================================================================================================================================================
'''def show_employee(name,salary=9000):
    return name,salary
print(show_employee("ramesh"))
    '''

##output:
##    ('ramesh', 9000)
##    


##===================================================================================================================================================================




#6.a. Write a Python function that takes a number as a parameter and check the number is prime or not.

'''def prime(a):
    for i in range(2,a+1):
        if a%i==0:
            print("not a prime")
            break
    else:
        print("prime number")
a = int(input("enter number"))

prime(a)'''

##output:
##enter number9
##not a prime

##===================================================================================================================================================================


##6b. Write a Python function that checks whether a passed number is palindrome or not.


'''def palledrome(a):
    if str(a)[::-1]==str(a):
        print("pallendrome number")
    else:
        print("not a pallendrome number")
a = int(input("enter number"))

palledrome(a)'''
##output:
##enter number11
##pallendrome number


##===================================================================================================================================================================


##7. 	a. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


'''
a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
b = a.sort(key=lambda x:x[a])
print(b)
'''

##output:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
##===================================================================================================================================================================


##7b. 	Write a Python program to create Fibonacci series upto n using Lambda






##c.  Write a Python program to add two given lists using map and lambda.
'''a =[1,5,6,8,9]
b =[9,8,8,7,5]

c = list(map(lambda x,y:x+y,a,b))
print(c)'''
##output:
##    
##[10, 13, 14, 15, 14]
##===================================================================================================================================================================

##d. Write a Python program to find palindromes in a given list of strings using Lambda.  
##Orginal list of strings:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##List of palindromes:
##['php', 'aaa']
'''
a =['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

b = list(map(lambda x: x[::-1]==x,a))
print(b)
'''
##output:
##[True, False, False, False, False, True]
##===================================================================================================================================================================

##e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
##(Hint: lambda will be passed to sort method's key parameter as argument)

##===================================================================================================================================================================




##f. Write a lambda function which takes z as a parameter and returns z*11
##



##===================================================================================================================================================================


##8. 	a. Using List Comprehension Find all of the numbers from 1–1000 that are divisible by 8
'''
a =[i for i in range(1000) if i%8==0]
print(a)
'''

##output:
##    [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640, 648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792, 800, 808, 816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952, 960, 968, 976, 984, 992]


##===================================================================================================================================================================


##b. Use list comprehension to contruct a new list but add 6 to each item.

'''b = [4,5,6,4,5,6]
a = [ i+6 for i in b]
print(a)'''
##output:
##    [10, 11, 12, 10, 11, 12]


##===================================================================================================================================================================

##
##9. string = "Practice Problems to Drill List Comprehension in Your Head."
##•	Remove all of the vowels in a string (use string above)
##•	Find all of the words in a string that are less than 5 letters (use string above
##•	Use a dictionary comprehension to count the length of each word in a sentence (use string above)


'''string = "Practice Problems to Drill List Comprehension in Your Head."
c = 'aeiou'
c =[]
for i in string.split():
    if len(i)<5:
        a = [j for j in i if j  not in c]
        print(a)
        
        print(len(a),end=' ')'''


##
##output:
##    ['t', 'o']
##['L', 'i', 's', 't']
##['i', 'n']
##['Y', 'o', 'u', 'r']
#2 4 2 4     
    




##===================================================================================================================================================================

##10. First, create a range from 100 to 160 with steps of 10.
##Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.

'''a =[i for i in range(100,160,10)]
print(a)
for i in a:
    if i%100==0:
        print(i)
##output:
##    [100, 110, 120, 130, 140, 150]
#100
'''








##===================================================================================================================================================================
##11. Using dict comprehension and a conditional argument create a dictionary from the current dictionary where
#only the key:value pairs with value above 2000 are taken to the new dictionary. dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}


##===================================================================================================================================================================

##12. Write a Python Set comprehension with an if clause example
##
####
##
##
##

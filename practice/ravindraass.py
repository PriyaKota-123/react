'1. Define a function that accepts roll number and returns whether the student is present or absent.'
##def fun(rollnumber):
##    if rollnumber==21:
##        print('student is absent')
##    else:
##        print('student is present')
##        
##num = int(input('>:'))
##fun(num)

##output:
##>:23
##student is present

'2. a. Write a python program to print multiple arguments.'
##def foo(name,age,gender):
##    print(name,age,gender)
##
##name = 'ravindra'
##age = 23
##gender = 'Male'
##foo(name,age,gender)
##
##output:
##ravindra 23 Male

    
'b. Write a function that accepts variable length key value pair as arguments.'
##def foo(**kwargs):
##    print(args)
##
##foo(name='Ravi',age=23,gender='male')
##
##output:
##{'name': 'Ravi', 'age': 23, 'gender': 'male'}


'3. a. Write a python program to find the power of a number using recursion'
##def fun(num,power,c):
##     if power>1:
##        num = num*c
##        power -= 1
##        fun(num,power,c)
##     if power==1:
##         print(num)
##        
##num = 12
##power = 4
##c = num
##fun(num,power,c)
##
##output:
##    20736


'b. Write a Python program of recursion list sum Test Data: [1, 2, [3,4], [5,6]] Expected Result: 21'

##def fun(lst):
##    add = 0
##    for i in range(len(lst)):
##        if type(lst[i])== list:
##            add += fun(lst[i])
##        else:
##    
##            add=add+lst[i]
##    return add        
##            
##lst = [1,2,[3,4],[5,6]]
##print(fun(lst))




'''4. Create an inner function to calculate the addition in the following way

Create an outer function that will accept two parameters, a and b

Create an inner function inside an outer function that will calculate the addition of a and b

At last, an outer function will add 5 into addition and return it'''
##def fun(a,b):
##    def inner():
##        c = a+b
##        return c
##    return inner()+5
##
##a = 9
##b = 6
##print(fun(a,b))
##
##output:
##    20




'5. a. Assign a different name to function and call it through the new name'
##def fun():
##    print(65)
##
##diff = fun()
##diff
##
##output:
##    65



'''b. 15.Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both,
and if the salary is missing in function call it should show it as 9000'''
##def show(name, salary=9000):
##    print(name)
##    print(salary)
##    
##name = 'Arvain'
##salary = 2000
##show(name,salary)
##show(name)
##
##output:
##    Arvain
##    2000
##    Arvain
##    9000


'6. a. Write a Python function that takes a number as a parameter and check the number is prime or not.'

##def prime(num):
##    for i in range(2,num):
##        if num%i==0:
##            print('it is not a prime number')
##            break
##    else:
##        print('it is a prime number')
##
##num = int(input('>:'))
##prime(num)
##
##output:
##    >:19
##    it is a prime number


'b. Write a Python function that checks whether a passed number is palindrome or not.'
##def palin(num):
##    string = str(num)
##    if string == string[::-1]:
##        print('it is a palindrome')
##    else:
##        print('it is not a palidrome')
##num = int(input('>:'))
##palin(num)
##
##output:
##    >:123454321
##    it is a palindrome
##




'''7. a. Write a Python program to sort a list of tuples using Lambda. Original list of tuples:
    [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''

##tup = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##
##tup.sort(key=lambda x:x[1])
##print(tup)
##
##output:
##    [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



'b. Write a Python program to create Fibonacci series upto n using Lambda'
##lst = [0,1]
##print(0,1,end=' ')
##
##for i in range(5):
##    b = lambda x:x[-2]+x[-1]
##    print(b(lst),end=' ')
##    lst.append(b(lst))
##    
##output:
##    0 1 1 2 3 5 8 


'c. Write a Python program to add two given lists using map and lambda.'
##lst1 = [1,2,3,4]
##lst2 = [5,6,7,8]
##add = list(map(lambda x,y:x+y,lst1,lst2))
##print(add)
##
##output:
##    [6, 8, 10, 12]


'''d. Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings: ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] List of palindromes: ['php', 'aaa']'''

##strings = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##lst = list(filter(lambda x:x==x[::-1],strings))
##print(lst)
##
##output:
##    ['php', 'aaa']



'''e. Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.

(Hint: lambda will be passed to sort method's key parameter as argument)'''

##lst = [5,6,12,3,4]
##lst.sort(key=lambda x:-x)
##
##print(lst)
##
##output:
##    [12,6,5,4,3]



'f. Write a lambda function which takes z as a parameter and returns z*11'
##x = lambda z:print(z*11)
##x('fs')
##
##output:
##    fsfsfsfsfsfsfsfsfsfsfs


'8. a. Using List Comprehension Find all of the numbers from 1–1000 that are divisible by 8'
##lst = [i for i in range(1,1000) if i%8==0]
##print(lst)
##
##output:
##    [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224,
##     232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432,
##     440, 448, 456, 464, 472, 480, 488, 496, 504, 512, 520, 528, 536, 544, 552, 560, 568, 576, 584, 592, 600, 608, 616, 624, 632, 640,
##     648, 656, 664, 672, 680, 688, 696, 704, 712, 720, 728, 736, 744, 752, 760, 768, 776, 784, 792, 800, 808,
##     816, 824, 832, 840, 848, 856, 864, 872, 880, 888, 896, 904, 912, 920, 928, 936, 944, 952, 960, 968, 976, 984, 992]



'b. Use list comprehension to contruct a new list but add 6 to each item.'
##lst = [2,3,4,5,6]
##lst2 = [i+6 for i in lst]
##print(lst2)
##
##output:
##    [8, 9, 10, 11, 12]


'9. string = "Practice Problems to Drill List Comprehension in Your Head."'

'· Remove all of the vowels in a string (use string above)'

##string = "Practice Problems to Drill List Comprehension in Your Head."
##vowels = 'aeiou'
##
##lst = ''.join([i for i in string if i not in vowels])
##print(lst)
##
##output:
##    Prctc Prblms t Drll Lst Cmprhnsn n Yr Hd.


'· Find all of the words in a string that are less than 5 letters (use string above)'
##string = "Practice Problems to Drill List Comprehension in Your Head."
##lst2 = string.split(' ')
##five = [i for i in lst2 if len(i)<5]
##print(five)
##
##output:
##    ['to', 'List', 'in', 'Your']



'· Use a dictionary comprehension to count the length of each word in a sentence (use string above)'
##string = "Practice Problems to Drill List Comprehension in Your Head."
##lst2 = string.split(' ')
##dic = {i:len(i) for i in lst2}
##print(dic)
##
##output:
##    {'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}




'''10. First, create a range from 100 to 160 with steps of 10.

Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.'''
##lst = [i for i in range(100,160,10)]
##
##dic = {i:i%100 for i in lst}
##print(dic)
##
##output:
##    {100: 0, 110: 10, 120: 20, 130: 30, 140: 40, 150: 50}


'''11. Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with
value above 2000 are taken to the new dictionary. dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}'''
##dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
##
##dict2 = {i:dict1[i] for i in dict1 if dict1[i]>2000}
##print(dict2)
##
##output:
##    {'NFLX': 4950, 'TREX': 2400}


'12. Write a Python Set comprehension with an if clause example'
##set1 = {i for i in range(1,10) if i%2==0}
##print(set1)
##
##output:
##    {8, 2, 4, 6}


















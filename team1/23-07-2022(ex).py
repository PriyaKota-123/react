'''1.Write a Python program to get all possible combinations of the elements of a given list using itertools module.'''

##from itertools import *
##l=[1,2,3,4,5,6,7]
##print(list(combinations(l,2)))
##print("-----------------------------------------------------------------")
##print(list(combinations(l,3)))
##print("-----------------------------------------------------------------")
##print(list(combinations(l,4)))



'''2.Write a python program to create an iterator that returns consecutive keys and groups from an iterable..'''

##import itertools 
##l=[('a',1),('b',2),('c',3),('d',4)]
##a=lambda x:x[0]
##for key,group in itertools.groupby(l,a):
##    print(key+":",list(group))

##import itertools
##a=[('a',1),('b',2),('c',3)]
##b=lambda x:x[0]
##for key,group in itertools.groupby(a,b):
##    print(key+":",list(group))

'''3. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150.'''
##
##from datetime import date
##def years():
##    for i in range(2000,2151):
##        def isSunday(i):
##            return 6==date(i,12,25).weekday()
##        if isSunday(i):
##            print(i)
##years()



##from datetime import date
##def years():
##    for i in range(2000,2151):
##        def isSunday(i):
##            return 6==date(i,12,25).weekday()
##        if isSunday(i):
##            print(i)
##years()



from datetime import date
def years():
    for i in range(2000,2030):
        def isSunday(i):
            return 6==date(i,12,25).weekday()
        if isSunday(i):
            print(i)
years()
'''4.write a python program using generator write armstrong'''
##def arm():
##    a=input("enter a number")
##    b=len(a)
##    sum=0
##    for i in a:
##        sum=sum+int(i)**b
##    c=int(a)
##    if sum==c:
##        yield "armstrong"
##    else:
##       yield "not armstrong"
##for j in arm():
##    print(j)
##    

'''5.write a python program by using math module use 3 function for each function one example.'''
'''combinations'''
##import math
##a=34
##b=9
##print(math.comb(a,b))

'''factorial'''

##import math
##print(math.factorial(9))
##print(math.factorial(23))


'''sum'''

##import math
##print(math.fsum([1,2,3,4,5]))
##print(math.fsum([34,56,78]))
##print(math.fsum([12,45,67,89]))

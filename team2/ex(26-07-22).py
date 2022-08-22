"""1.. Write a Python program that invoke a given function after specific milliseconds. 
inputs:100ms-16
1000ms-100
2000ms-25100
Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858"""

##from time import*
##import math
##
##def Late(fn, ms, *args):
##  sleep(ms / 1000)
##  return fn(*args)
##
##
##print("Square root after Specific Miliseconds:") 
##print(Late(lambda x: math.sqrt(x), 100, 16))
##print(Late(lambda x: math.sqrt(x), 1000, 100))
##print(Late(lambda x: math.sqrt(x), 2000, 25100))
##

"""2  we will provide two lists list_1 and list_2.
 The list_1 and list_2 of this function represent the initial list. Need to comprehend by list:
1Multiply each value in the two lists separately
2Add each value in the two lists separately
3Multiply the values in the two lists
by using inner and outer functions """



"""3.Write a Python program to build a list, using an iterator function and an initial seed value.

1.The iterator function accepts one argument (seed) and must always return a list
with two elements ([value, nextSeed]) or False to terminate.
2.Use a generator function, fn_generator, that uses a while loop
to call the iterator function and yield the value until it returns False.
3.Use a list comprehension to return the list that is produced by the generator, using the iterator function."""

##def iterator(seed):
##    lst = [3]
##    lst.append(seed)
##    return lst
##
##def gener(num):
##    while True:
##        yield iterator(num)
##
##lst2 = [next(gener(i)) for i in range(10)]
##print(lst2)
##      


"""4.Write a Python program to create Cartesian product of two or more given lists using itertools."""


##import itertools 
##def cartesian_Product(lists):
##    return list(itertools.product(*lists))
##
##ls=[12,13],[30,40]
##print("The Original List:",ls)
##print("The Cartesian Product List Is:",cartesian_Product(ls))


"""5.Write a Python program to count the frequency of the elements of a given unordered list by using itertools."""

##from itertools import groupby
##
##lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
##
##print("Original list:",lst)
##
####lst.sort()
####print("\nSort the said unordered list:",lst)
##result={}
##for i in lst:
##     if i in result:
##         result[i]+=1
##     else:
##         result[i]=1
##print("The Frequency of the List is ",result)

import itertools
lst = [1,1,1,1,2,2,2,1,1,5,5,5]
for i,j in itertools.groupby(lst):
    print(len(list(j)))

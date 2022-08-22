##1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty

'''l=[1,2,3,4,5,6,7]
a=len(l)
index=0
position=3-1
while a>0:
    index=(index+position)%a
    print(l.pop(index))
    a-=1

output:
3
6
2
7
5
1
4'''
##
##2).. Write a Python program to count the number of students of individual class.
##Sample Output:
##Counter({'VI': 3, 'V': 2, 'VII': 1})

'''from collections import Counter
c=(('V',1),('I',6),('III',1),('VII',7),)
s=Counter(class_name for class_name ,no_student in c)
print(s)
'''

##3).Write a Python program to concatenate all elements in a list into a string and return it

'''def fun(list):
    result=" "
    for i in list:
        result +=str(i)
    return result
print(fun([1,2,3,4,5]))

output:

 12345
'''    


##4).Write a Python program to convert a float to ratio. 
##Expected Output :
##21/5
'''from fractions import Fraction
v=4.2
a=Fraction(v).limit_denominator()
print(a)

output:

21/5'''
##5).Write a Python function that prints out the first n rows of Pascal’s triangle
'''def pascal(n):
    row=[1]
    y=[0]
    for x in range(max(n,0)):
        print(row)
        row=[l+r for l,r in zip(row+y,y+row)]
    return n>=1
pascal(6)


output:

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]'''


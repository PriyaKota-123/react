#6.Find the mean of a list.

'''l=[1,2,3,4,5,6,7,8,9,10]
l2=(1+2+3+4+5+6+7+8+9+10)
l3=l2/10
print(l3)

output:

5.5
'''

##7.Take a list and perform list operation
#append
'''1.append
l=[1,2,3,4,5]
l.append(6)
print(l)

output:
[1, 2, 3, 4, 5, 6]
'''
#clear
'''l=[1,2,3,4]
l.clear()
print(l)

output:

[]'''

#copy
'''l=[1,2,3,4,5]
l2=l.copy()
print(l2)
print(l)

output:

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
'''


#count
'''l=[1,2,3,4]
count=0
for i in l:
    count=count+i
    print(count)
output:
1
3
6
10
'''
#extend
'''l=[1,2,3,4]
l2=[5,6,7,8]
l.extend(l2)
print(l)

output:
[1, 2, 3, 4, 5, 6, 7, 8]
'''
#index
'''l=[1,2,3,4]
print(l.index(3))
output:
2'''

#insert
'''l=[1,2,3,45]
l.insert(1,6)
print(l)

output:
[1, 6, 2, 3, 45]
'''
#pop
'''l=[1,2,3,4,5,6]
l.pop()
print(l)

output:
[1,2,3,4,5]
'''

#pop(index)
'''l=[1,2,3,4,5,6]
l.pop(3)
print(l)
output:
[1, 2, 3, 5, 6]
'''
#remove
'''l=[1,2,3,4,5,6]
l.remove(2)
print(l)

output:
[1, 3, 4, 5, 6]
'''
#reverse
'''l=[1,3,5,6]
l.reverse()
print(l)

output:
[6, 5, 3, 1]'''

#sort
'''l=[1,2,3,456,0,40,9,4,56,67]
l.sort()
print(l)

output:
[0, 1, 2, 3, 4, 9, 40, 56, 67, 456]
'''

##8.Collatz Sequence
'''def fun(n):
    while n!=1:
        print(n, end=" ")
        if n & 1:
            n=3*n+1
        else:
            n=n//2
            
    print(n)
print(fun(6))

output:
6 3 10 5 16 8 4 2 1
None'''

'''def fun(a):
    while a!=1:
        print(a,end=" ")
        if a & 1:
            a=3*a+1
        else:
            a=a//2
    print(a)
print(fun(6))'''

##9.Find the midpoint of a line

'''a=2
b=5
a1=67
b1=6
x=(a+a1)/2
y=(b+b1)/2
print(x)
print(y)

output:

34.5
5.5
'''
##10.Get the values in one list and keys in another from a dictionary.

'''d={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(d.keys())
print(d.values())

output:
dict_keys([1, 2, 3, 4, 5])
dict_values(['one', 'two', 'three', 'four', 'five'])
'''
#========================================================================
'''d={1:"one",2:"two",3:"three",4:"four",5:"five"}
b=list(d.keys())
c=list(d.values())
print(b)
print(c)

output:

[1, 2, 3, 4, 5]
['one', 'two', 'three', 'four', 'five']
'''

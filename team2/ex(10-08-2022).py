##1.Python Program to Reverse a Stack using Recursion

'''def a(n,ls):
    if len(n)==0:
        print(ls)
    else:
        m=n.pop()
        ls.append(m)
        a(n,ls)
lst=[1,2,3,4,5]
lst2=[]
a(lst,lst2)

output:

 [5, 4, 3, 2, 1]'''

##2.Python Program to Append the Content of One File to the End of Another File

'''n=input("enter file to be read from")
n1=input("enter file to be append to")
f=open(n,"r")
d=f.read()
f.close()
f1=open(n1,"a")
f1.write(d)
f1.close()'''

##3.Python Program to Create a Class and Get All Possible Distinct Subsets from a Set

'''class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))

output:

[[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''



##4.How can you randomize the items of a list in place in Python?
'''import random
a=["kavya bonnam","ajju bonnam","picklu"]
random.shuffle(a)
print(a)

output:

 ['kavya bonnam', 'picklu', 'ajju bonnam']'''

##5.write a python program on showing 
##KeyboardInterrupt
'''try:
  n=input("enter a number")
  print("try  error occured")
except KeyboardInterrupt:
    print("keyboardinterrupt error occurred")
    
output:

enter a number
keyboardinterrupt error occurred'''


##ArithmeticError
'''a=10
b=0
try:
    c=a/b
    print(c)
except ArithmeticError:
    print("Arithmetic error occured")

output:

Arithmetic error occured'''


##StopIteration
'''l=[1,2,3]
l1=iter(l)
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))

output:

1
2
3
Traceback (most recent call last):
  File "C:\pk22105\team2\ex(10-08-2022).py", line 95, in <module>
    print(next(l1))
StopIteration'''

    
##AssertionError
'''a=10
b=2
assert a<b,'Invaliderror'

output:

Traceback (most recent call last):
  File "C:\pk22105\team2\ex(10-08-2022).py", line 111, in <module>
    assert a<b,'Invaliderror'
AssertionError: Invaliderror'''

    
##ImportError


'''from itertools import shuffle
a=[1,2,3]
a.shuffle()
print(a)


output:

Traceback (most recent call last):
  File "C:\pk22105\team2\ex(10-08-2022).py", line 124, in <module>
    from itertools import shuffle
ImportError: cannot import name 'shuffle' from 'itertools' (unknown location)'''


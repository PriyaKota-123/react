
#string methods
#1.isalpha()
'''s="priya123"
print(s.isalpha())

output:
False
'''
'''def fun(a):
    for i in a:
        if i.isalpha():
            return "true"
        else:
            return "false"
a=input()
print(fun(a))

output:

mounika
true
'''

#2.isdigit()

'''def fun(a):
    for i in a:
        if a.isdigit():
            return "true"
        else:
            return "false"
a=input()
print(fun(a))

output:
67
true'''



'''d={1:"jith",2:"nhgur"}
r=list(d.keys())
t=list(d.values())
print(r)
print(t)'''



#3.isalnum()

'''def fun(a):
    for i in a:
        if i.isalnum():
            return "true"
        else:
            return "false"
a=input()
print(fun(a))

output:

pur756
true
'''

#4.lower()

'''def funa(a):
    print(a.lower())
a=input()
funa(a)

output:
MOunika
mounika
'''

'''a="AHFKGKUHR"
print(a.lower())

output:

ahfkgkuhr
'''

#5.upper()

'''def fun(a):
    print(a.upper())
a=input()
fun(a)

output:

priya is a good girl
PRIYA IS A GOOD GIRL
'''

#6.tittle()

'''def fun(a):
    print(a.title())
a=input()
fun(a)

output:

priya
Priya
'''


#7.split()

'''def fun(a):
    print(a.split())
a=input()
fun(a)

output:
priya
['priya']
'''

'''a=input("enter a string")
for i in a:
    x=a.count(i)
    print(x,i)


a=input().split()
x=a.count("priya")
print(x)'''


#8.strip()
#it will remove both leading and trailing characters(based on ther arguments passed) 
'''a="geeks for geeks"
print(a)
b="ekgs"
print(a.strip(b))

output:
geeks for geeks
 for 
'''

'''a="priya priya"
print(a)
b="rypa"
print(a.strip(b))

output:

priya priya
riya priy

priya priya
iya pri
'''


#9.replace()

'''a="priya"
print(a)
b=a.replace('p','k')
print(b)

output:
priya
kriya
'''

#10.join()
'''a="priya"
b="*".join(a)
print(b)

output:

p*r*i*y*a
'''
'''def fun(a):
    print("".join(a))
a="priya"
fun(a)

output:
priya'''

#11.endswith()
'''a="priya"
print(a.endswith('a'))

output:
True'''    

#12.startswith()

'''a="priya"
print(a.startswith('p'))

output:
True'''

#13.partitions()
'''a="picky pickulu vicky"
print(a,'after partitions',a.partition("picky"))

output:

picky pickulu vicky after partitions ('', 'p', 'icky pickulu vicky')
picky pickulu vicky after partitions ('', 'picky', ' pickulu vicky')'''


#14.rpartition()

'''a="picky#pickulu#"
print(a,a.rpartition('#'))

output:

picky#pickulu# ('picky#pickulu', '#', '')
'''

#15.find()

'''a="priya is a good girl"
print(a.find('good'))

output:
11'''

#16.rfind()
'''
a="priya is a good girl"
b=a.rfind('ood')
print(b)

output:
12'''

#17.index
'''a="rani is a good girl"
b="a"
c=a.index(b,2)
print(c)

output:
8
'''
#18.format()
'''a="{} is a {} boy."
print(a.format("pickulu","good"))

output:
pickulu is a good boy.
'''
#19.splitlines()
'''a="Cat\nBat\nSat\nMat\nXat\nEat"
print(a.splitlines())

output:
['Cat', 'Bat', 'Sat', 'Mat', 'Xat', 'Eat']
'''

#20.capitalize()
'''a="priya is a good girl"
print(a.capitalize())

output:
Priya is a good girl
'''

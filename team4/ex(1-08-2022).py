##1.write a python program do multiplication program using generators and use sys module to find memory size

'''import sys
def multi(a):
    for i in range(1,a+1):
        yield a*i
for i in (multi(5)):
    print(i)
a=sys.getsizeof(i)
print(a)

#output:
5
10
15
20
25
28'''


##2..write a python program do multiplication program using function

'''def multi(a):
    for i in range(1,a+1):
        print(a*i)

multi(5)

#output:
5
10
15
20
25'''
    

##3.Write a Python program to extract characters from various text files and puts them into a list.

'''f=open("data.txt","r")
f1=open("text1.txt","r")
a=[]
#d=f.read()
for i in [f,f1]:
    d=i.read()
    a.append(d)
    print(a)
f.close()
f1.close()


#output:

['ghdghuijskfGFUIO\nGJGDUGWIGDGWEUTNBCX DH\nHJEOYWEIWYVBN KWL\nHWOIHDBSB\n']
['ghdghuijskfGFUIO\nGJGDUGWIGDGWEUTNBCX DH\nHJEOYWEIWYVBN KWL\nHWOIHDBSB\n', 'vxbncguwqibj\nuUIWQHJDGUW\nBNDVB\njhhffojchoyf\nkhfoiyoei,bd\n']'''


##4. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.

'''import string
def letters(n):
    with open("data.txt","w") as f:
        alphabet=string.ascii_uppercase
        l=[alphabet[i:i+n]+"\n" for i in range(0,len(alphabet),n)]
        f.writelines(l)
letters(5)'''


##5.write a python program in twin prime using outer and inner functions
'''def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def  twins(start,end):
    for i in range(start,end):
        j=i+2
        if(prime(i) and prime(j)):
            print("{:d} and {:d}".format(i,j))
twins(2,100)


output:
3 and 5
5 and 7
11 and 13
17 and 19
29 and 31
41 and 43
59 and 61
71 and 73'''


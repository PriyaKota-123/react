##1) take a list and output has to be repeated of the second half of the list elements
##input = [1,2,3,4,5,6]
##output = [4,5,6,4,5,6]

'''l=[1,2,3,4,5]
b=len(l)//2
l[:b]=l[b:]
print(l)


output:

[3, 4, 5, 3, 4, 5]'''

##2) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)


'''s="pk22105"
if s.isalnum():
    print("string matched")
else:
    print("don't matched")


output:

string matched'''

##3) Write a Python program that matches a string that has an a followed by zero or more b's.

'''n=input("enter a string")
if n[0]=='a' and n[-1]=='b':
    print("A given string matched")
else:
    print("not matched")

output:

enter a stringaabb
A given string matched'''


##4) Write a Python program that matches a word at the beginning of a string.

'''word='the'
s="the vicky is a good lazy boy"
l=s.split(' ')
if l[0]==word:
    print("word is matched")
else:
    print("word don't matched")
 output:

word is matched'''

##5) open a file and enter a lists like each list is having two or more elements in to the file and retrieve their details in the ouput in lists.

'''l=[1,2,3]
with open("text1.txt","w+") as f:
    f.write(f'{l}')
with open("data1.txt","r") as f:
    k=f.read()
    print(k)
'''

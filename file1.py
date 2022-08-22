##1.Write a Python program to read last n lines of a file.

'''f=open("text1.txt","r")
d=f.readlines()
n=int(input("enter a number:"))
print("last line",d[-n:])
f.close()'''

##2.Write a Python program to read a file line by line and store it into a list.

'''f=open("text1.txt","r+")
d=f.readlines()
e=[]
for i in d:
    e.append(i)
    print(e)
f.close()
'''
##3.Write a Python program to read a file line by line store it into a variable.

'''f=open("text1.txt","r+")
d=f.readlines()
e=""
for i in d:
    e=e+i
print(e)
f.close()'''



##5. Write a Python program to count the frequency of words in a file

'''f=open("text1.txt","r+")
d=f.read()
count=0
for i in d.split():
    count=count+1
    print(count)
f.close()'''



'''import collections
with open('text1.txt',"r") as f:
    r=f.read()
    print(collections.Counter(r))'''

##6. Write a Python program to read a random line from a file.

##import random
##f=open("text1.txt","r")
##d=f.readline()
##print("")

'''import random
def ran(file):
    a=open(file).read().splitlines()
    return random.choice(a)
print(ran("text1.txt"))
'''    
##7.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

'''import string ,os
if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_uppercase:
    with open(letter+".txt","w") as f:
        f.writelines(letter)'''

##8.Write a Python program to extract characters from various text files and puts them into a list.

'''f=open("text1.txt","r")
f1=open("data.txt","r")
e=[]
for i in [f,f1]:
    k=i.read()
    e.append(k)
    print(e)
f.close()
f.close()'''

##9.Write a Python program that takes a text file as input and returns the number of words of a given text file
##Note: Some words can be separated by a comma with no space.

'''def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("text.txt"))
'''



##10.Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line


import string
def letters_file_line(n):
   with open("text1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)

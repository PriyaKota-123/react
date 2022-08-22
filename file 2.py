#File Handling 

#1.Write a program in python to replace all word “the” by another word “them” in a file “poem.txt”.
'''
f=open("poem.txt")
d=f.read()
d=d.replace("the","them")
f.close()
f=open("poem.txt","w")
f.write(d)
f.close()'''


#2.Write a program in python to replace a character by another character in a file “story.txt”. (Accept both the characters from the user)
'''f = open("story.txt")
d = f.read()
a = input("Enter character to be replaced")
b = input("Enter character that will replaced")
d = d.replace(a,b)
f.close()
f = open("story.txt","w")
f.write(d)
f.close()'''


##Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”.
'''f = open("data.txt", "r")
d = f.read()
d = d.replace('a', '@')
f.close()
f=open("data.txt", "w")
f.write(d)
f.close()'''

##
##Write a program in python to read file “data.txt” and display only those lines whose length is more than 40 characters.
'''
f = open("data.txt","r")
d = f.readlines()
for i in d:
    if len(i) > 40:
        print(i)'''

##
##Write a program in python to remove all duplicate lines from the file “story.txt”.

'''
f = open("story1.txt", "r")
d = f.readlines()
m = [ ]
for i in d:
     if i not in m:
        m.append(i)
print(m)
f.close()
f = open("story1.txt", "w")
for i in m:
     f.write(i)   
f.close()'''




##
##Write a program in python to display only unique words from the file “story.txt”.

'''f = open("story.txt", "r")
d = f.read()
d = d.split()
str = " "
m = []
for i in d:
  if i not in str:
       str=str+i
       print(i, end=" ")
f.close()'''

##
##Write a program in python to count the frequency of each vowels in a file “task.txt”.


'''f = open("task.txt", "r")
d = f.read()
va=ve=vo=vu=vi=0
for i in d:
     if i=='a' or i=='A':
         va=va+1
     if i=='e' or i=='E':
         ve=ve+1
     if i=='i' or i=='I':
         vi=vi+1
     if i=='o' or i=='O':
         vo=vo+1
     if i=='u' or i=='U':
         vu=vu+1
print("Frequency of vowel \"a\" is", va)
print("Frequency of vowel \"e\" is", ve)
print("Frequency of vowel \"i\" is", vi)
print("Frequency of vowel \"o\" is", vo)
print("Frequency of vowel \"u\" is", vu)'''


##
##Write a program in python to count those words whose length is more than 7 characters in a file “story.txt”.
'''f=open("story.txt", "r")
d=f.read()
d=d.split()
c=0
for i in d:
  if len(i)>7:
    c=c+1
print("Total words are :", c)'''
##
##Write a program in python to count those lines from the file “div.txt” which are starting from ‘T’ or ‘M’.

'''f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] == 'M' or i[0] == 'T':
        c=c+1
print("Total lines are :", c)'''

##
##Write a program in python to count those lines from the file “div.txt” which are not starting from ‘M’.

'''f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] != 'M':
        c=c+1
print("Total lines are :", c)'''



##
##Write a program in python to display those words from a file “image.txt” which are ending from alphabet ‘m’.

'''f=open("image.txt",'r')
d=f.read()
d=d.split()
c=0
for i in d:
    if i[-1]=='m':
        c=c+1
print("Total words are :", c)'''


##
##Write a program in python to read all lines of file “data.txt” using readline() only.


'''f=open("data.txt")
d=f.readlines()
print(d)
f.close()'''



##
##Write a program in Python to copy the entire content from file “data.txt” to “story.txt”
'''
f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read()
e = f1.write(d)
f.close()
f1.close()
print(e)

'''




##
##Write a program in Python to copy the alternate lines from file “data.txt” to “story.txt
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.readlines()
for i in range(len(d)):
    if i%2==0:
        print(i)
f.close()
f1.close()'''

##
##Write a program in Python to read the entire content from file “data.txt” and copy the contents to “story.txt” in upper case.
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read().upper()
e = f1.write(d)
f.close()
f1.close()
print(e)'''

##
##Write a program in Python to read the entire content from file “data.txt” and copy only those words to “story.txt” which start from vowels.

'''
f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read().lower()
e = d.split()
for i in e:
    if  i[0] in ['a', 'e', 'i', 'o', 'u']:
        f1.write(i)
f.close()
f1.close()
print(e)'''


##
##Write a program in Python to read the entire content from file “data.txt” and copy only those words in separate lines to “story.txt” which are starting from lower case alphabets .
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d = f.read().lower()
e = f1.write(d)
f.close()
f1.close()
print(e)
'''

##
##Write a program in Python to read file “data.txt” and copy only those lines to “story.txt” which are starting from alphabets “A” or “T”.
'''f = open("data.txt", "r")
f1 = open("story.txt","w")
d=f.read()
e =d.split()
for i in e:
     if i[0] == 'M' or i[0] == 'T':
        f1.write(i)
f.close()
f1.close()
'''
##
##Write a program in Python which display the longest word from file “star.txt”

'''f = open("star.txt", "r")
d = f.read()
L = d.split()
longword = " "
for i in L:
    if  len(i) > len(longword):
      longword = i
print("longest word is ,",longword)
f.close()

'''



##
##Write a program in Python which display the longest line from file “star.txt”
'''f = open("star.txt", "r")
d = f.readlines()
longline = " "
for i in d:
    if  len(i) > len(longline):
      longline = i
print("longest line is : ", longline)
f.close()'''

##
##Write a program in Python to read the file “star.txt” and display the entire content after removing leading and trailing spaces.
'''f = open("star.txt", "r")
d = f.readlines()
for i in d:
    print(i.strip())
f.close()
'''


##
##Write a program in python that read the content from file “sumit.txt” and display all numbers.

'''f = open("sumit.txt", "r")
d = f.read()
for i in d:
    if i.isdigit():
        print(i)
f.close()
'''


##
##Write a program in Python that display the second and second last line from the file “life.txt”
'''f = open("life.txt", "r")
d = f.readlines()
print("Second line is :",d[1])
print("Second last line is :",d[-2])
f.close()'''

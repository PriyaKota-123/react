'''create a-z  of 26 files and write a different sentence in each file and delete all files by using os module
filenames should be 1.a.file,2.b.file........26.z.file
in each file each sentence is to start with character of  its own filename
after entering data delete all the files'''
import string
import os
strg = string.ascii_lowercase
for i in strg:
    with open(i+'.txt','w') as f:
        f.write(i+'anand')

for i in strg:
    os.remove(i+'.txt')
    

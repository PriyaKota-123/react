#1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-

'''import re
def char(s):
    c=re.compile(r'[^a-zA-Z0-9]')
    s=c.search(s)
    return not bool(s)
print(char("ADFaagg123"))
print(char("*&%@#!}{"))
output:
True
False
'''


#without using functions
'''import re
s="ADFasgg34"
c=re.compile(r'[^a-zA-Z0-9]')
s=c.search(s)
print(not bool(s))

output:
True'''


#2. Write a Python program that matches a string that has an a followed by zero or more b's

'''import re
s="ab"
p='^a(b*)$'
if re.search(p,s):
    print("found")
else:
    print("not found")

output:
found'''


#3.Write a Python program that matches a string that has an a followed by one or more b's.

'''import re
s="aaab"
p='ab+?'
if re.search(p,s):
    print("found")
else:
    print("not found")

output:
found'''


#4. Write a Python program that matches a string that has an a followed by zero or one 'b'.

'''import re
s="adcfdb123"
p="ab?"
if re.search(p,s):
    print("found")
else:
    print("not found")

output:

found'''

#5. Write a Python program that matches a string that has an a followed by three 'b'

'''import re
s="abbb"
p='ab{3}?'
if re.search(p,s):
    print("found")
else:
    print("not found")
output:

found'''

#6.Write a Python program that matches a string that has an a followed by two to three 'b'.

'''import re
s="abb"
p="ab{2,3}"
if re.search(p,s):
    print("found")
else:
    print("not found")
output:

found'''

#7. Write a Python program to find sequences of lowercase letters joined with a underscore.

'''import re
s="achjhv_fuf"
p="^[a-z]+_[a-z]+$"
if re.search(p,s):
    print("found")
else:
    print("not")

output:

found'''

#8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

'''import re
s="AFGGajlifoe"
p="^[A-Z]+[a-z]+$"
if re.search(p,s):
    print("found")
else:
    print("not")
output:
found'''

#9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re
s=""

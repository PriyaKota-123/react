#1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-

##import re
##s="hi priya kota 1233"
##p=re.compile(r'[^a-zA-z0-9]')
##a=p.search(s)
##print(a)

import re
def char(s):
    c=re.compile(r'[^a-zA-Z0-9]')
    s=c.search(s)
    return not bool(s)
print(char("ADFaagg123"))
print(char("*&%@#!}{"))



import re
s="ADFasgg34"
c=re.compile(r'[^a-zA-Z0-9]')
s=c.search(s)
print(bool not,(s))

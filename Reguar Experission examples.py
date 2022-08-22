#1.Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-

import re
s="hi priya kota 1233"
p=(r'[^a-zA-z0-9]')
r=re.search(s,p)
print(r)

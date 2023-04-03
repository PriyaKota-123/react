##import re
##string="hello 2 hi 89.HOwdy 34"
##pattern="\d+"
##result=re.findall(pattern,string)
##print(result)
##

##import re
##s="Twelve :12 Eight nine :89"
##pattern="\d+"
##r=re.split(pattern,s)
##print(r)
##
##

'''import re
count=0
p=re.compile("ab")
s=p.finditer("abaaababaabbaab")
for i in s:
    count=count+1
    print("original index:",i.start())

output:
original index: 0
original index: 4
original index: 6
original index: 9
original index: 13'''

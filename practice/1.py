##import copy
##old_list= [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
##new_list= copy.copy(old_list)
##old_list.append([4,  4, 4])
##print("Old list:", old_list)
##print("New list:", new_list)

##
##from copy import deepcopy
##person1 = ["Swen", ["Seestrasse",  "Konstanz"]]
##person2 = deepcopy(person1)
####person2[0]  = "Sarah"
##print(person1)
##print(person2)

##d={'Name':'Pratyusha','Age':24,'Role':'Trainer'}
##d['Age']=27
##print(d)

##def fun(a):
##    b=[]
##    
##    
##    for i in a:
##        b.append((len(i),i))
##        b.sort()
##       
##    return b[-1]
##   


a=["ramesh","mounika","correcidal","priya"]
b=[]
for i in a:
    b.append(i)
print(max(b))

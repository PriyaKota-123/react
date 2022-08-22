##1) create a list of combinations of entered number like below
##input: 5
##list must be created as [4,4,4,3,3,2,2,1,1,1]
##if input: 7
##list must be created as [6,6,6,5,5,4,4,3,3,2,2,1,1,1]
##first decending number and number 1 should be repeated three times
##

##
##from itertools import combinations
##n=input("enter a value")
##a=combinations(n,2)
##print(list(a))

a=int(input())
b=[]
for i in range(a-1,0,-1):
    if i==1 or i==a-1:
        b.append(i)
        b.append(i)
        b.append(i)
    else:
        b.append(i)
        b.append(i)
print(b)

output:
5
[4, 4, 4, 3, 3, 2, 2, 1, 1, 1]
     

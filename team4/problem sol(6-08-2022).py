###write a python program on sprial number using inner function
##and decorator
##eg:-1 2 3
##    8 9 4
##    7 6 5
n = 1
order = [0,1,2,5,8,7,6,3,4]
lst = [1,2,3,4,5,6,7,8,9]
for i in order:
    lst[i]=n
    n+=1
print(lst)

m = 0
for i in lst:
    print(i,end=" ")
    m+=1
    if m%3==0:
        print()

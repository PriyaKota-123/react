##1) take a list of 8 numbers
##lst = [1,2,3,4,5,6,7,8]
##and add the alternative numbers in list 
##
##after first iteration list should be [4,6,8,10,12,14]
##after second iteration [12,16,20,24]
##after third iteration [32,40]
##
##when list is having two elements print that list in the output

'''lst = [1,2,3,4,5,6,7,8]
lst2 = []
while len(lst)!=2:
    
    for i in range(len(lst)-2):
        k = lst[i] + lst[i+2]
        lst2.append(k)
    lst = lst2
    lst2 = []
    print(lst)

output:

[4, 6, 8, 10, 12, 14]
[12, 16, 20, 24]
[32, 40]
'''    

##4.Please complete the code in solution.py to realize the function of get_sum. get_sum function receives an array parameter nums. Please use the lambda function to pass 
##in two unknown number x and y for the get_sum function and take this lambda function as the return value of the get_sum function. For the parameter nums received by get_sum, 
##if the length of the array num is an even number, return the sum of nums by x times. If the length of the array num is an odd number, return the sum of nums by -y times.
##input:[1,2,3,4]
##       2,3
##output:20
##import functools
##nums1 = [2,3,5,6,76,4,3,2]
##sq =functools.reduce(lambda x,y:x+y,nums1)
##print(sq)
##
##l=[1,2,3,4,5,6]
##s=list(map(lambda x:x+x,l))
##print(s)

l=[1,2,3,4]
x=lambda l:sum(l)
if x(l)%2==0:
    print(x(l)*2)
else:
    print(x(l)*-3)

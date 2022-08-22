##1).Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
##and then check whether they are divisible by 5 or not.
##The numbers that are divisible by 5 are to be printed in a comma separated sequence.
##
##Example:
##0100,0011,1010,1001
##Then the output should be:
##1010
##Notes: Assume the data is input by console.


'''value = []
a=int(input())
items=[x for x in a().split(',')]
for p in items:
    b= int(p, 2)
    if not b%5:
        value.append(p)

print( ','.join(value))'''


##2).Write a menu driven program which shows all operations on Binary File 
##
##Add Record 
##
##Display All Record 
##
##Display Specific Record 
##
##Modify Record 
##
##Delete Record 
##
##Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type

'''import pickle
def addrec():
     L=[ ]
     f=open("data.dat","ab")
     rn = int(input("Enter Room Number"))
     pr = int(input("Enter the price of room"))
     rt = input("Enter the type of room")
     L  = [rn, pr, rt]
     pickle.dump(L, f)
     print("Record added in the file")
     f.close()
addrec()

output:

Enter Room Number5
Enter the price of room8
Enter the type of roomop
Record added in the file'''



##3).Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat”
##whoose model number (integer type) is passed as an argument.
##Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price]

import pickle
def addval():
     L=[ ]
     f=open("mobile.dat","ab")
     mid = int(input("Enter Mobile id"))
     mb = input("Enter the brand of mobile")
     mn = input("Enter the model number of mobile")
     pr = int(input("Enter the price of Mobile"))
     L  = [mid, mb, mn, pr]
     pickle.dump(L, f)
     print("Record added in the file")
     f.close()
addval()

##output:
##
##Enter Mobile id12
##Enter the brand of mobileiphone
##Enter the model number of mobilebo
##Enter the price of Mobile678899
##Record added in the file'''


##4).Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and
##the values are square of keys.

'''def Dict():
	d=dict()
	d[1]=1
	d[2]=2**2
	d[3]=3**2
	print(d)
Dict()

output:
    {1: 1, 2: 4, 3: 9}'''


##5).Please write a program using generator to print the numbers which can be
##divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
##
##Example:
##If the following n is given as input to the program:
##
##100
##
##Then, the output of the program should be:
##
##0,35,70


'''def Generator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input("Enter a Number."))
values = []
for i in Generator(n):
    values.append(str(i))

print (",".join(values))


output:
Enter a Number.100
0,35,70'''


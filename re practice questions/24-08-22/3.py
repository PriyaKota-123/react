##11) WAPP to reverse internal content of every second word present in the given String.


##a="priya is a good girl".split()
##b=""
##for i in len(a):
##    c=int(i)
##    if i%2!=0:
##        b.append(c)
##        print(b)
##

'''a="priya is a good girl is has a long hair".split()
print(a)
b=[]
i=0
while i<len(a):
    if i%2==0:
        b.append(a[i])
    else:
        b.append(a[i][::-1])
    i=i+1
print(" ".join(b))


output:

['priya', 'is', 'a', 'good', 'girl', 'is', 'has', 'a', 'long', 'hair']
priya si a doog girl si has a long riah
'''

##12) WAPP for the following requirements
##    input->a3z2b4
##    output->aaabbbbzz(sorted string).

'''a="a3z2b4"
b=""
d=""
for i in a:
   if i.isalpha():
       c=i
   else:
      b=b+c*int(i)
x=sorted(b)
for i in x:
    d=d+i
print(d)

#output:

aaabbbbzz'''


##13)WAPP  to extract year ,month,date and time using lambda Function.

'''import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
time=lambda x:x.time()
month=lambda x:x.month
day=lambda x:x.day
print(year(now))
print(time(now))
print(month(now))
print(day(now))


output:
2022-08-24 15:04:30.960363
2022
15:04:30.960363
8
24'''
#yesterday date example
'''from datetime import date
from datetime import timedelta
today=date.today()
print(today)
yesterday=today-timedelta(days=1)
print(yesterday)

output:
2022-08-24
2022-08-23
'''

##14)WAPP to find the values of length six in given list using lambda Function.

'''a=["priyaa","picky","vicky","pickul","rani","venky"]
r=list(filter(lambda x:len(x)==6,a))
print(r)
output:
['priyaa', 'pickul']
'''


##15)WAPP to find factorial of number using closure Function.

'''def fun():
    def fun1():
        n=int(input())
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    return fun1()
print(fun())

output:
5
120
'''

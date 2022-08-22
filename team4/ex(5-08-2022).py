##1) write a program on magical method add , pos and neg?

#POS
'''class emp:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __pos__(self):
        print(self.a)
        print(self.b)
e=emp(3,-22)
+e'''

#neg

'''class emp:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __neg__(self):
        print(self.a)
        print(self.b)
e=emp(-3,-22)
-e'''

#add

'''class emp:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b
e=emp(3)
print(e+6)'''

##2) write a program convert day number to date in particular year?
'''from datetime import datetime
day="30"
print("the day number"+str(day))
a=day.rjust(3+len(day),'0')
print(a)
year="2020"
res=datetime.strptime(year + "-" + day,"%Y-%d")
print("resolved"+ str(res))'''

##3) write a dictionary to a file in python?

'''dict={1:"priya",2:"picky",3:"vicky"}
with open("data2.txt","w") as f:
    f.write(str(dict))'''


##4) find the most repeated word in a text file?

'''with open("text1.txt","r") as f:
    f.read()
    print("",f.read())
with open("data.txt","w") as f1:
    f.write()
    print("",f.write())'''


##5) write a program on sprial number?
##eg:-1 2 3
##    8 9 4
##    7 6 5







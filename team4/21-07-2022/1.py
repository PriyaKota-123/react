'''1.Write a python program in fibonacci series using generator'''

##def fib(limit):
##    a,b=0,1
##    while a<limit:
##        yield a
##        a,b=b,a+b
##x=fib(8)
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print("using for in loop")
##for i in fib(8):
##    print(i)
##   



'''2.Write a python program to generate the running product of the elemnts of a given iterable'''



##def product():
##    a=4
##    b=5
##    c=a*b
##    yield c
##for i in product():
##    print(i)



'''3.factorial using iterators'''

##def fact(x):
##    a=1
##    for i in range(1,x+1):
##        a*=i
##        yield a
##for x in fact(6):
##    print(x)
##    



'''4.Write a simple registeration form which contains input buttons heading and radio buttons'''

##from tkinter import *
##a=Tk()
##a.geometry('500x600')
##a.title('simple registration')
##label=Label(a,text='Registration form',width=20,font=("bold",20))
##label.place(x=90,y=53)
##label1=Label(a,text="full name",width=20,font=("bold",10))
##label1.place(x=80,y=130)
##entry=Entry(a)
##entry.place(x=240,y=130)
##label2=Label(a,text="Email",width=20,font=("bold",10))
##entry_1=Entry(a)
##entry_1.place(x=240,y=130)
##label3=Label(a,text="gender",width=20,font=("bold",10))
##label3.place(x=70,y=230)
##var=IntVar()
##Radiobutton(a, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
##Radiobutton(a, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
##label4=Label(a,text="Age:",width=20,font=("bold",10))
##label4.place(x=70,y=280)
##entry_2=Entry(a)
##entry_2.place(x=240,y=280)
##Button(a,text='Submit',width=20,bg='yellow',fg='white'),place(x=180,y=360)
##a.mainloop()
##print("registration form successfully created...")


'''5.prime progam using sys module'''

##import sys
##a=int(input("enter a number"))
##for i in range(2,a):
##    if a%i==0:
##        print("not a prime")
##        break
##else:
##    print("prime")

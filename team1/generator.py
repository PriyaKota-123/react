def fun():
    a=int(input("enter a value"))
    b=int(input("enter a value"))
    c=a+b
    yield c
for i in fun():
    print(i)
##    print(next(i))
##    print(next(i))

from turtle import  *
#chnage the pen speed
speed(10)
def insta1(x,y):
    penup()
    goto(x,y)
    pendown()
def insta2(x,y,f,c,c1,c2):
    color(c)
    insta1(x,y)
    begin_fill()
    for i in range(4):
        forward(f)
        circle(c1,c2)
    end_fill()
def insta3(c,x,y,c1):
    color(c)
    begin_fill()
    insta1(x, y)
    circle(c1)
    end_fill()

#controllers
insta2(-150,-120,350,"pink",20,90)
insta2(-110,-70,260,"white",20,90)
insta2(-90,-50,220,"pink",20,90)
insta3("white",20,10,70)
insta3("pink",20,30,50)
insta3("white",110,160,15)
hideturtle()
done()

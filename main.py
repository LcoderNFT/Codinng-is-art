#1
from turtle import *
bgcolor('black')
color('cyan')
speed(11)
hideturtle()
n = 1
p = True
while True:
    circle(n)
    if p:
        n = n - 1
    else:
        n = n - 1
        left(1)
    if n == 0 or n == 60: 
        p = not p
        forward(0.3)

#2
from turtle import *
Music Note

    
    width(20)
    bgcolor('black')
    colors = ['#db0f3c', '#50ebe7', 'white']
    for col in colors:
        up
    goto(0,0)
    color(col)
    left(180)
    circle(50, 270)
    forward(120)
    left(180)
    circle(50, 90)
    
#3
color('white')
bgcolor('black')
left(185)
hideturtle()
begin_fill()
circle(30, 200)
forward(200)
left(173)
forward(190)
circle(-18, 170)
end_fill()
done()

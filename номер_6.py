from turtle import *
tracer(0)
screensize(3000,3000)
c=25
lt(90)
rt(30)
for i in range(10):
    fd(30*c)
    rt(60)
    fd(30*c)
    rt(120)
up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*c,y*c)
        if x == 0 or y == 0:
            dot(3, 'red')
        else:
            dot(3, 'blue')
update()
exitonclick()


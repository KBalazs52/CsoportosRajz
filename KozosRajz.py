#jelzolampa teste, hatterszin K. Balázs
#jelzolampa felso resze es fenyek H. Bálint


#jelzolampa fekete negyzet

import turtle

turtle.fillcolor("black")
turtle.begin_fill()

i = 0
while i < 4:
    if i % 2:
        turtle.forward(200)
    else:
        turtle.forward(100)
    turtle.left(90)
    i += 1

turtle.end_fill()

#körök

turtle.goto(50, 10)

i = 0
while i < 3:
    if i == 0:
        turtle.fillcolor("green")
    elif i == 1:
        turtle.fillcolor("yellow")
    else:
        turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.pendown()
    i += 1

#vissza az alaphoz
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.done()
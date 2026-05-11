#jelzolampa teste, hatterszin K. Balázs

#jelzolampa felso resze es fenyek H. Bálint

#alap beallitasok
import turtle
turtle.speed(0)
turtle.color("Gray")
#pozicio
turtle.penup()
turtle.forward(25)
turtle.pendown()
#hatter szine
turtle.bgcolor("DarkSlateGray1")
#jelzolampa szine
turtle.fillcolor("Gray")
turtle.begin_fill()
#jelzolampa alja
i=0
while i<2:
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    i+=1

turtle.end_fill()
turtle.done()
import turtle
import numpy as np

turtle.shape('arrow')
turtle.color('yellow')
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.color('black')
turtle.circle(70)
x = 0
y = 0
turtle.penup()
x -= 30
y += 70
turtle.goto(x, y)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
x += 60
turtle.goto(x, y)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
y -= 10
x -= 30
turtle.goto(x, y)
turtle.color('black')
turtle.pendown()
turtle.width(5)
turtle.seth(-90)
turtle.forward(20)
turtle.penup()
x -= 30
y -= 15
turtle.color('red')
turtle.goto(x, y)
turtle.pendown()
for i in range(50):
	turtle.left(360/100)
	turtle.forward(2)
turtle.mainloop()
import turtle
import numpy as np

turtle.shape('arrow')
turtle.right(90)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
for i in range(6):
	turtle.circle(30, -180)
	turtle.circle(7, -180)

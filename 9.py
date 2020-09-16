import turtle
import numpy as np

turtle.shape('arrow')
def draw(k, step):
	for j in range(k):
		turtle.forward(step)
		turtle.left(360/k)
r = 50
step = 40
x = 0
y = 0
z = 0
turtle.seth(0)
for i in range(3, 11, 1):
	r = step / (2 * np.sin(180 / i))
	turtle.seth(90 + 180 / i)
	draw(i,step)
	step += 10
	x += 10
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
turtle.mainloop()

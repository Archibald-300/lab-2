import turtle
import numpy as np

turtle.shape('arrow')
k = 66
r = 200
f = 0
f =(r * np.sin(2 * np.pi / k)) / np.sin(np.pi / k)

turtle.speed(0)
turtle.penup()
turtle.goto(0, r)
turtle.pendown()
turtle.seth(-90 + 180 / k )
if k % 4 == 0:
	
	for i in range(k):
		turtle.forward(f)
		turtle.right(180 - (360 / k))

elif k % 2 == 0:
	turtle.seth(-90 + 180 / k )
	for i in range(k // 2):
		turtle.forward(f)
		turtle.right(180 - (360 / k))
	turtle.penup()
	turtle.goto(0,-r)
	turtle.pendown()
	for i in range(k // 2):
		turtle.backward(f)
		turtle.right(180 - (360 / k))

if k % 2 == 1:
	turtle.penup()
	turtle.goto(r/4, -r)
	turtle.pendown()
	for i in range(k):
		turtle.right(180 - 180 / k )
		turtle.forward(f)

turtle.mainloop()
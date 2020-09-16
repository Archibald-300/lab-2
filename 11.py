import turtle
import numpy as np

turtle.shape('arrow')
turtle.speed(0)
def draw(k,step):
	for j in range(k):
		turtle.forward(step)
		turtle.left(360/k)
def dr(k,step):
	for j in range(k):
		turtle.forward(step)
		turtle.right(360/k)



go = 1.0
turtle.left(90)
for i in range(1, 5, 1):
	go += 0.5
	draw(100, go)
	dr(100, go)
turtle.mainloop()
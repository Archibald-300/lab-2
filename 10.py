import turtle
import numpy as np

turtle.shape('arrow')
def draw(k):
	for j in range(k):
		turtle.forward(2)
		turtle.left(360/k)


g = 6
for i in range(g):
	turtle.left(360/g)
	draw(100)
turtle.mainloop()
	

import turtle

turtle.shape('arrow')
num = 7
for i in range(num):
	turtle.forward(50)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(50)
	turtle.left(180-360/num)
turtle.mainloop()


import turtle

turtle.shape('arrow')
x = 0
y = 0
for i in range(10):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	for j in range(4):
		turtle.left(90)
		turtle.forward(20 * i)
	y -= 10
	x += 10
turtle.mainloop()


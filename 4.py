import turtle

turtle.shape('arrow')
turtle.penup()
turtle.goto(0, -40)
turtle.pendown()
for i in range(200):
	turtle.left(360 / 200)
	turtle.forward(4)

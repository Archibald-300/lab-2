import turtle
k = 0
turtle.shape('arrow')
for j in range(5):
	for i in range(100):
		k += 1
		turtle.forward(0.01 * k)
		turtle.left(3.6)
turtle.mainloop()

import turtle

turtle.shape('turtle')

'''
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
'''

# 사각형
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

# 삼각형
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

# 원
turtle.circle(50)


turtle.mainloop()

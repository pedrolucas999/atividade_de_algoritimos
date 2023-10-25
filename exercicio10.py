import turtle
import random

leo = turtle.Turtle()


for _ in range(4):
    leo.shape('turtle')
    leo.color("red")
    leo.forward(100)
    leo.right(90)
    
leo.penup()
leo.forward(200)
leo.pendown()

for _ in range(4):
    leo.shape('circle')
    leo.color('blue')
    leo.forward(100)
    leo.right(90)
leo.left(90)
leo.penup()
leo.forward(50)
leo.pendown()

for _ in range(4):
    leo.shape('square')
    leo.color('black')
    leo.forward(100)
    leo.right(90)

leo.left(90)
leo.penup()
leo.forward(100)
leo.pendown()

for _ in range(4):
    leo.shape('triangle')
    leo.color('green')
    leo.forward(100)
    leo.right(90)

leo.penup()
leo.forward(120)
leo.left(90)
leo.pendown()

leo.forward(160)
for _ in range(4):
    leo.shape('arrow')
    leo.color('orange')
    leo.left(90)
    leo.forward(350)
    
    





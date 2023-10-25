import turtle
import random

def random_color():
    r = random.random()
    b = random.random()
    g = random.random()
    return(r,b,g)
leo = turtle.Turtle()
leo.pensize(5)

leo.left(2)
leo.color('red')
leo.right(160)
leo.forward(100)
leo.color('blue')
leo.right(45)
leo.forward(100)
leo.color("green")
leo.right(157)
leo.forward(188)
leo.right(90)
    
for _ in range(3):
    pen_color=random_color()
    leo.pencolor(pen_color)
    leo.forward(188)
    leo.right(90)
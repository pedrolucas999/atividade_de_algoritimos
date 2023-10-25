import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (16):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(22.5)
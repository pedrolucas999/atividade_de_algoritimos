import turtle
import random

leo = turtle.Turtle()
leo.pensize(10)
colors = ['green', 'purple', 'blue']

for _ in range(3):
    color = random.choice(colors)
    leo.color(color)
    
    leo.forward(100)
    leo.left(120)
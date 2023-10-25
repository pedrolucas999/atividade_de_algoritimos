import turtle
import random

leo = turtle.Turtle()
colors = ['red', 'purple', 'blue']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    leo.color(color)
    leo.forward(100)
    leo.left(120)
          
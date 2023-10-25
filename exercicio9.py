import turtle
import random
leo = turtle.Turtle()
colors = ['blue', 'red', 'pink', 'yellow']



for c in range(360):
    color = random.choice(colors)
    leo.color(color)
    leo.forward(2)
    leo.right(1)
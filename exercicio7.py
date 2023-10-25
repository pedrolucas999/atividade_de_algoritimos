import turtle

leo = turtle.Turtle()
leo.pensize(1)

for color in ['pink', 'red', 'black', 'blue']:
    leo.color(color)
    leo.forward(100)
    leo.left(90)

leo.penup()
leo.forward(150)
leo.pendown()

for color in ['blue', 'red', 'black', 'pink']:
    leo.color(color)
    leo.forward(100)
    leo.left(90)
    
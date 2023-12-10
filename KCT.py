import turtle

# Create turtle object
t = turtle.Turtle()

# Draw a square
for i in range(10):
    t.forward(100)
    t.left(90)

# Hide turtle
t.hideturtle()

# Keep window open until closed
turtle.done()

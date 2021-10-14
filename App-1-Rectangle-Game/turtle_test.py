import turtle

# Create canvas
myturtle = turtle.Turtle()

# Move turtle (drawing)
myturtle.penup() # Lift pen
myturtle.goto(50, 75)

# Draw rectangle
myturtle.pendown() # Put down pen
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()
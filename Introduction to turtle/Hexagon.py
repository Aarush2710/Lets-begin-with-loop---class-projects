import turtle
screen=turtle.Screen()
screen.setup(800,600)
screen.title("Test")
screen.bgcolor("blue")
board=turtle.Turtle()
sides=6
side_lengh=100
angle=360/sides
for i in range (sides):
    board.forward(side_lengh)
    board.right(angle)

turtle.done()

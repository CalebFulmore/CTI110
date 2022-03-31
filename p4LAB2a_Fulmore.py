#import and style the shape
import turtle
turtle.shape("turtle")
turtle.pensize(3)
turtle.color("brown")

#to draw the square
for i in range(4): 
    turtle.forward(50)
    turtle.left(90)
#to draw the triangle
for i in range(3):
    turtle.forward(50)
    turtle.left(120)
turtle.exitonclick()

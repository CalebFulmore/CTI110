import turtle
turtle.shape("turtle")
turtle.pensize(5)
turtle.color("lightblue")

''' For the letter C '''
turtle.speed(1)
turtle.backward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.backward(50)

''' The space '''
turtle.penup()
turtle.backward(20)
turtle.pendown()

''' And the letter F '''
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.backward(40)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.exitonclick()

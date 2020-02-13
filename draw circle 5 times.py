import turtle
pen=turtle.Turtle()

for i in range(6):

    pen.circle(20*i)
    pen.up()
    pen.sety((20*i)*(-1))
    pen.down()
    pen.end_fill()
turtle.done()

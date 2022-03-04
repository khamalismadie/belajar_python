import turtle

pen = turtle.Turtle()
def ring(col,rad):
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()

pen.up()
pen.setpos(-35,95)
pen.down
ring('black', 15)

pen.up()
pen.setpos(35,95)
pen.down
ring('black', 15)

pen.up()
pen.setpos(0,35)
pen.down
ring('white', 40)

pen.ip()
pen.setpos(-18,75)
pen.down
ring('black', 8)



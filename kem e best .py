import turtle

wn = turtle.Screen()
bird = turtle.Turtle()
bird.speed(13)
bird.pensize(4)
bird.color("black")
bird.setpos(-75, 0)
bird.fillcolor("pink")

bird.begin_fill()
for i in [0, 1, 2]:
    bird.circle(30, 360)
    bird.forward(1)
    bird.forward(174)
    bird.left(120)
bird.end_fill()
bird.penup()
bird.forward(175)
bird.pendown()
bird.begin_fill()
bird. left (300)
for i in [0, 1, 2]:
    bird.circle(30, 360)
    bird.forward(175)
    bird.left(120)
bird.fillcolor("pink")

bird.end_fill()

bird.forward(25)
bird.right(90)


bird.fillcolor("PeachPuff")
bird.begin_fill()
bird.end_fill()

#for i in [0, 1, 2]:
    #bird.fd(125)
    #bird.left(90)

bird.end_fill()

bird.pendown()
bird.color("orange")

bird.fillcolor("white")

bird.begin_fill()

bird.end_fill()
bird.hideturtle()

bird.penup()
bird.forward(300)
bird.pendown()
bird.left(90)
bird.forward(100)
bird.left(90)
bird.forward(100)
bird.back(100)
bird.left(90)
bird.forward(100)
bird.left(270)
bird.forward(100)
bird.backward(100)
bird.left(270)
bird.forward(50)
bird.left(90)
bird.forward(100)
bird.penup()
bird.forward(50)
bird.pendown()
bird.left(90)
bird.forward(50)
bird.back(100)
bird.forward(100)
bird.penup()
bird.forward(20)
bird.pendown()
bird.fillcolor("pink")
bird.begin_fill()
bird.circle(15, 360)
bird.end_fill()
style = ('Courier', 30, 'italic')
bird.write('kem e best!', font=style, align='center')
bird.penup()
bird.left(90)
bird.forward(100)
bird.pendown()

bird.write('einar!', font=style, align='center')

wn.exitonclick()


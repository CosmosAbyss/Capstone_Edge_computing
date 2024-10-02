import turtle
p = turtle.Pen()
p.speed(0)
p.pensize(3)
#face
p.setheading(160)
turtle.colormode(255)
p.fillcolor(255,245,178)
p.begin_fill()
p.circle(60, 200)
p.forward(200)
p.right(30)
p.circle(40,270)
p.circle(40,-20)
p.setheading(90)
p.circle(95,155)
p.end_fill()
# eyebrow_big
#left
p.penup()
p.goto(40,25)
p.pendown()
p.setheading(0)
p.pensize(10)
p.circle(-20,50)
p.circle(-20,-10)
#right
p.penup()
p.goto(100,25)
p.pendown()
p.setheading(0)
p.pensize(10)
p.circle(-20,50)
p.circle(-20,-100)


# eyebrow_small
#left
p.penup()
p.goto(40,10)
p.pendown()
p.setheading(0)
p.pensize(2)
p.circle(-25,80)
p.circle(-25,-160)
#right
p.penup()
p.goto(100,10)
p.pendown()
p.setheading(0)
p.pensize(2)
p.circle(-25,80)
p.circle(-25,-160)


# Eyes
# Left
p.penup()
p.goto(40,-25)
p.pendown()
p.pencolor("black")
p.dot(40)
p.pencolor("white")
p.dot(15)
# Right
p.penup()
p.goto(100,-25)
p.pendown()
p.pencolor("black")
p.dot(30)
p.pencolor("white")
p.dot(10)

# Mouth
p.penup()
p.goto(20,-100)
p.pendown()
p.pencolor(151,82,87)
p.dot(50)

# hair
p.penup()
p.goto(15,30)
p.pendown()
p.setheading(45)
p.pencolor("black")
p.pensize(23)
p.circle(-87,140)


turtle.done()
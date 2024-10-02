import turtle
import random


turtle.setup(width=800, height=900)
p = turtle.Pen()
p.speed(0)
turtle.colormode(255)

# face function
def draw_face(p, x, y):
    p.penup()
    p.goto(x, y)
    p.pendown()
    
    # face
    p.setheading(160)
    p.fillcolor(255, 245, 178)
    p.begin_fill()
    p.circle(60, 200)
    p.forward(200)
    p.right(30)
    p.circle(40, 270)
    p.circle(40, -20)
    p.setheading(90)
    p.circle(95, 155)
    p.end_fill()

    # eyebrow_big
    # left
    p.penup()
    p.goto(x+40, y+25)
    p.pendown()
    p.setheading(0)
    p.pensize(10)
    p.circle(-20, 50)
    p.circle(-20, -10)
    
    # right
    p.penup()
    p.goto(x+100, y+25)
    p.pendown()
    p.setheading(0)
    p.circle(-20, 50)
    p.circle(-20, -100)

    # eyebrow_small
    # left
    p.penup()
    p.goto(x+40, y+10)
    p.pendown()
    p.setheading(0)
    p.pensize(2)
    p.circle(-25, 80)
    p.circle(-25, -160)
    
    # right
    p.penup()
    p.goto(x+100, y+10)
    p.pendown()
    p.setheading(0)
    p.pensize(2)
    p.circle(-25, 80)
    p.circle(-25, -160)

    # Eyes
    # Left
    p.penup()
    p.goto(x+40, y-25)
    p.pendown()
    p.pencolor("black")
    p.dot(40)
    p.pencolor("white")
    p.dot(15)

    # Right
    p.penup()
    p.goto(x+100, y-25)
    p.pendown()
    p.pencolor("black")
    p.dot(30)
    p.pencolor("white")
    p.dot(10)

    # Mouth
    p.penup()
    p.goto(x+20, y-100)
    p.pendown()
    p.pencolor(151, 82, 87)
    p.dot(30)

    # Hair
    p.penup()
    p.goto(x+15, y+30)
    p.pendown()
    p.setheading(45)
    p.pensize(23)
    p.pencolor("black")
    p.circle(-87, 140)



# making popart with 3*3 chessboard
def draw_pop_art():
    colors = [(255, 192, 203), (173, 216, 230), (255, 165, 0), (144, 238, 144), (221, 160, 221), (255, 182, 193), (240, 230, 140), (64, 224, 208), (255, 127, 80)]
    
    p.speed(0)
    
    for row in range(3):
        for col in range(3):
            x = col * 350 - 450
            y = row * 350 - 450

    
            # random background color
            p.penup()
            p.goto(x, y)
            p.pendown()
            p.setheading(360)
            p.fillcolor(random.choice(colors))
            p.begin_fill()
            for _ in range(4):
                p.pensize(10)
                p.forward(300)
                p.left(90)
            p.end_fill()

             # face in chessboard
            draw_face(p, x+50 , y+150 )


        

draw_pop_art()

turtle.done()

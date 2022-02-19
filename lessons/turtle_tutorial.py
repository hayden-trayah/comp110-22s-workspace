from turtle import Turtle, color, colormode, done
leo: Turtle = Turtle()

"""Draws a square manually"""
# leo.forward(200)
# leo.left(90)
# leo.forward(200)
# leo.left(90)
# leo.forward(200)
# leo.left(90)
# leo.forward(200)
# leo.left(90)

"""Square"""
colormode(255)
color()
# leo.color(99, 204, 10)
# leo.begin_fill()
# i: int = 0
# while (i < 4):
#     leo.forward(200)
#     leo.left(90)
#     i = i + 1
# leo.end_fill()
    
# leo.penup()
# leo.goto(45, 60)
# leo.pendown()

# leo.pencolor("pink")
# leo.fillcolor(32, 67, 93)
# leo.color("green", "yellow")

"""Triangle"""
colormode(255)
leo.color(0, 0, 0)
leo.speed(10)
leo.hideturtle()
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(200)
    leo.left(120)
    i = i + 1
leo.end_fill()
    
done()
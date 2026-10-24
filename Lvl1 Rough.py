import turtle

t = turtle.Turtle()
t.shape('turtle')

t.penup()
t.hideturtle()

t.speed(0)
#Line in the middle
t.goto(480,0)
t.pendown()
t.goto(-480,0)
t.goto(100,0)
#Backdrop
s = turtle.Screen()
s.setup(width=800, height=600)
s.colormode(255)

t_sky = turtle.Turtle()
t_sky.speed(0)
t_sky.hideturtle()
t_sky.penup()

color_start = (255, 100, 0)
color_end = (50, 0, 150)
num_lines = 300

for i in range(num_lines):
    ratio = i / (num_lines - 1)
    new_r = int(color_start[0] * (1 - ratio) + color_end[0] * ratio)
    new_g = int(color_start[1] * (1 - ratio) + color_end[1] * ratio)
    new_b = int(color_start[2] * (1 - ratio) + color_end[2] * ratio)
    
    t_sky.pencolor(new_r, new_g, new_b)
    t_sky.goto(-400, i)
    t_sky.pendown()
    t_sky.forward(800)
    t_sky.penup()

t_sun = turtle.Turtle()
t_sun.speed(0)
t_sun.hideturtle()
t_sun.penup()
#sun
t_sun.goto(0, 0)
t_sun.fillcolor("yellow")
t_sun.pencolor("yellow")
t_sun.begin_fill()
t_sun.setheading(90)
t_sun.circle(150, 180)
t_sun.left(90)
t_sun.forward(300)
t_sun.end_fill()
#sea
t.pencolor('Blue1')
t.pendown
t.fillcolor('Blue1')
t.begin_fill()
t.goto(480,0)
t.goto(480,-180)
t.goto(-480,-180)
t.goto(-480,0)
t.goto(480,0)
t.end_fill()

t.pencolor('dark blue')
t.pendown
t.fillcolor('dark blue')
t.begin_fill()
t.goto(480,-180)
t.goto(480,-360)
t.goto(-480,-360)
t.goto(-480,-180)
t.goto(480,-180)
t.end_fill()
#Sun eyes
t.penup()
t.hideturtle()
t.goto(0,0)
t.left(180)
t.setheading(90)
t.goto(-180,75)
t.pencolor('black')
t.pendown()
t.circle(25)
t.goto(-190,75)
t.dot(20)

t.penup()
t.hideturtle()
t.goto(0,0)
t.left(160)
t.setheading(90)
t.goto(-160,75)
t.pencolor('black')
t.pendown()
t.circle(-25)
t.goto(-150,75)
t.dot(20)
#smile
t.penup()
t.goto(0,0)
t.goto(-125,40)
t.pencolor('red')
t.pensize(8)
t.pendown()
t.setheading(-90)
t.circle(-35, 180)

t.hideturtle()


turtle.mainloop()
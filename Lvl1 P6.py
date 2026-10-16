import turtle
t= turtle.Turtle()
t.shape('turtle')
def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.goto(x1,y1)


def draw_rectangle(x0,y0, len, htg, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len , y0)
    draw_line(x0+len, y0, x0+len , y0+htg)
    draw_line(x0+len, y0+htg, x0, y0+htg)
    draw_line(x0, y0+htg, x0 , y0)
    t.end_fill()



    
n_rows = 20
n_cols = 20 
x_val  = -150
y_val  = 150


for jj in range(n_cols):
    if jj:




    draw_rectangle(x_val, y_val, 36, 36, "white")
    x_val = x_val + 20

for jj in range(20):



# https://www.youtube.com/watch?v=Lz0XK4qijUw (complicated color )

# Open this reffrence pic (https://i.pinimg.com/originals/61/ca/e6/61cae618654ae2b6abfd45913a5c5bdd.png)

turtle.mainloop()

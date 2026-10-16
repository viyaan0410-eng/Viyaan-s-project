import sys
import time

def type_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    return ''

import turtle

t = turtle.Turtle()
t.shape('arrow')
t.begin_fill()
t.penup()

t.speed(0)
t.pendown()
t.fillcolor('Red')
t.goto(100,0)

t.goto(100,100)

t.goto(0,100)

t.goto(0,0)

t.end_fill()


# Last Statement 
turtle.mainloop()
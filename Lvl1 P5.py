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
t.speed(0.6)

#ANimation

def eruption(offset):
    # volcano
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.fillcolor('#6B4F3A')
    t.begin_fill()
    
    t.goto(200,0)
    
    t.goto(60,200)
    
    t.goto(-60,200)
    
    t.goto(-200,0)
    
    t.end_fill()


    #ground
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.fillcolor("#1EFF00")
    t.begin_fill()
    
    t.goto(200,0)
    
    t.goto(200,-50)
    
    t.goto(-200,-50)
    
    t.goto(-200,50)
    
    t.end_fill()



    

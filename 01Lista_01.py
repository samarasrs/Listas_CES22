import turtle

def draw_squares(t, tam):
    for i in range(4):
        t.forward(tam)
        t.left(90)
    

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercício 01")

t=turtle.Turtle()

n=5
t.pen(fillcolor="magenta",pencolor="magenta", pensize=3)
for i in range(n):

    draw_squares(t,20+i*20)
    t.penup()
    t.setx((i+1)*-10)
    t.sety((i+1)*-10)
    t.pendown()
    
wn.mainloop()
            



    


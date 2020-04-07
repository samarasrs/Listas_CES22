import turtle

def draw_poly(t, n, sz):
    ang=360/n
    for i in range(n):
        t.forward(sz)
        t.setheading((i+1)*ang)
        
    

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercício 02")

t=turtle.Turtle()

t.pen(fillcolor="magenta",pencolor="magenta", pensize=3)

draw_poly(t,8,50)
wn.mainloop()
#
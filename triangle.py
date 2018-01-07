import turtle

def draw_triangle(some_pipi):
    for i in range(1,2):
        some_pipi.right(30)
        some_pipi.forward(100)
        some_pipi.right(120)
        some_pipi.forward(100)
        some_pipi.right(120)
        some_pipi.forward(100)

def draw():
    window = turtle.Screen()
    window.bgcolor("white")

    pipi = turtle.Turtle()
    pipi.speed(0)
    for i in range (1,361):
        draw_triangle(pipi)
        pipi.right(1)
        
    window.exitonclick()

draw()

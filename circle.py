import turtle

def draw_jajarangenjang(some_pipi):
    for i in range(1,2):
        some_pipi.left(35)
        some_pipi.forward(50)
        some_pipi.right(35)
        some_pipi.forward(50)
        some_pipi.right(145)
        some_pipi.forward(50)
        some_pipi.right(35)
        some_pipi.forward(50)

def draw():
    window = turtle.Screen()
    window.bgcolor("white")

    pipi = turtle.Turtle()
    pipi.speed(0)
    for i in range (1,37):
        draw_jajarangenjang(pipi)
        pipi.right(10)

    window.exitonclick()

draw()

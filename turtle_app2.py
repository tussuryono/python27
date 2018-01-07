import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow", "blue")
    brad.speed(1)
    
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("black")
    
    angie.circle(100)

    window.exitonclick()
    
draw_square()

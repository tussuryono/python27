import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)
        
def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow", "blue")
    brad.speed(1)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("black")
    
    #angie.circle(100)

    window.exitonclick()
    
draw()

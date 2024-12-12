#HM1
from turtle import *
speed(20)
width(7)

def triangle():
    color("green")
    begin_fill()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    end_fill()
    left(30)
    penup()
    forward(100)
    pendown()
    left(90)


for i in range(120):
    triangle()
exitonclick()

#HW 2
def hello_world():
    print("hello_world")

#HW 3
def even_or_odd(number):
    if number % 2 == 0:
        print("yes it is even")
    else:
        print("Yes, it is odd")

#HW 4
def draw_shapes():
    shapes = [
        "******\n******\n******",
        "     *\n    ***\n  *******\n***********\n     *\n     *",
        "*******\n *******\n  ********\n    ********"
    ]
    
    for shape in shapes:
        print(shape)
        print("n")

draw_shapes()

hello_world()

even_or_odd(23)  

draw_shapes()
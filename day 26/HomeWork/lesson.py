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
from turtle import *

#we want to paint hous

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)  
left(90) 
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #height of te door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("brown")
begin_fill()
left(30)
forward(80)
left(90)
forward(60)
left(90)
forward(80)
end_fill()
color("purple")
width(1)
right(90)
forward(140)
color("brown")
begin_fill()
width(7)
right(90)
forward(80)
right(90)
forward(60)
right(90)
forward(80)
end_fill()



exitonclick()    
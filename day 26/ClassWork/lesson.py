#შექვნათ ფუნცია turtle ში რომელსაც დავარქმევთ walk() რომელიც წავა 200 მოტრილავბეა მარცხნივ 90  შემდეგ ისევ უკან წამოვა და დდაგება თავის გზას
#fal_back() უკან უნდა დააბურნოს ჩვენი ისარი, საბოლოოდ 1 ფუნცქიით გააკეთოს ეს 2 მოქმედება:

from turtle import *
color("black")
def walk():
    forward(200)
    left(90)
color("yellow")
def fall_back():
    left(90)
    forward(200)

walk()
fall_back()
    

hideturtle()
exitonclick() 
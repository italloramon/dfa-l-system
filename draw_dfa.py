from turtle import *
from time import sleep

sequence = input("Type the correct sequence: ")
print("Load the screen...")
window = Screen()
window.bgcolor('cyan')
sleep(2)

turtle = Turtle()
turtle.speed(1)
turtle.color('red')

for letter in sequence:
    if letter == 'f':
        turtle.forward(10)
    elif letter == '+':
        turtle.left(10)
        turtle.forward(10)
    elif letter == '-':
        turtle.right(10)
        turtle.forward(10)

done()

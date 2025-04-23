#Marcus McRae
#04/23/25
#P4LAB1
#Use turtle and loops tp draw a square and a triangle

#Import the library
import turtle

#Create the turtle window and drawing objects
win = turtle.Screen()
pen = turtle.Turtle()

#Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

#Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)

#Whilw loop that excecutes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides  = sides - 1
    
    
#Wait for user to close window
win.mainloop()

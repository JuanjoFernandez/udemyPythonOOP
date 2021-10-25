import numpy as np
from PIL import Image

class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        canvas.img_array[self.x: self.x+self.side+1,
        self.y:self.y+self.side+1] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, canvas):
        canvas.img_array[self.x: self.x+self.height+1,
        self.y:self.y+self.width+1] = self.color


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.img_array = np.zeros((self.width, self.height, 3), dtype = np.uint8)
        if self.color == "white":
            self.img_array[:] = [255, 255, 255]

    def make(self):
        pass 

#############################################
##      CLI - Command Line Interface       ##
#############################################

# Creating the canvas
width = int(input("What's the width of the canvas in pixels?: "))
height = int(input("what's the height of the canvas in pixels?: "))
# Making sure the user chooses a right canvas color
valid_color = False
while valid_color == False:
    color = input("Choose a background color for your canvas (black/white): ")
    if color == "white" or color == "black":
        valid_color = True

canvas = Canvas(width, height, color)

# User drawings
end_of_program = False
while end_of_program == False:
    shape = input ("Choose the shape (square/rectagle) or type quit to fnish drawing: ")
    if shape == "square":
        square_x = int(input("Please provide starting x: "))
        square_y = int(input("Please provide starting y: "))
        square_side = int(input("Please give me the side length: "))
        square_red = int(input("How much red (0-255)? "))
        square_green = int(input("How much green (0-255)? "))
        square_blue = int(input("How much blue (0-255)? "))
        color = (square_red, square_green, square_blue)
        square = Square(square_x, square_y, square_side, color)
        square.draw(canvas)

    if shape == "rectangle":
        rec_x = int(input("Please provide starting x: "))
        rec_y = int(input("Please provide starting y: "))
        rec_width = int(input("Please give me the width length: "))
        rec_height = int(input("Please give me the height length: "))
        square_red = int(input("How much red (0-255)? "))
        square_green = int(input("How much green (0-255)? "))
        square_blue = int(input("How much blue (0-255)? "))
        color = (square_red, square_green, square_blue)
        rectangle = Rectangle(rec_x, rec_y, rec_width, rec_height, color)
        rectangle.draw(canvas)

    if shape == "quit":
        end_of_program = True

# Saving the image
img = Image.fromarray(canvas.img_array, 'RGB')
img.save('math_paint.png')
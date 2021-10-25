import numpy as np
from PIL import Image

class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        
        pass

class Rectangle:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
    
        pass


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


# Test inputs
width = 100
height = 100
color = "white"

# # Creating the canvas
# width = int(input("What's the width of the canvas in pixels?: "))
# height = int(input("what's the height of the canvas in pixels?: "))
# # Making sure the user chooses a right canvas color
# valid_color = False
# while valid_color == False:
#     color = input("Choose a background color for your canvas (black/white): ")
#     if color == "white" or color == "black":
#         valid_color = True

canvas = Canvas(width, height, color)

# Test inputs
# Square
square_x = 50
square_y = 50
square_side = 20
color = (100,150,200)
square.draw(canvas)

# # User drawings
# end_of_program = False
# while end_of_program == False:
#     shape = input ("Choose the shape (square/rectagle) or type quit to fnish drawing: ")
#     if shape == "square":
#         square_x = int(input("Please provide starting x: "))
#         square_y = int(input("Please provide starting y: "))
#         square_side = int(input("Please give me the side length: "))
#         square_red = int(input("How much red (0-255)? "))
#         square_green = int(input("How much green (0-255)? "))
#         square_blue = int(input("How much blue (0-255)? "))
#         color = (square_red, square_green, square_blue)
#         square = Square(square_x, square_y, square_side, color)
#         square.draw(canvas)

#     if shape == "rectangle":
#         pass

#     if shape == "quit":
#         end_of_program = True




# Saving the image
img = Image.fromarray(canvas.make(), 'RGB')
img.save('math_paint.png')
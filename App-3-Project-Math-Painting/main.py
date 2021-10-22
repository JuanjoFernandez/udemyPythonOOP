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
    
    def make(self):
        image_array = np.zeros((self.width, self.height, 3), dtype = np.uint8)
        if self.color == "white":
            image_array[:] = [255, 255, 255]
        return image_array

# Test inputs
width = 100
height = 100
color = "black"

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

# Saving the image
img = Image.fromarray(canvas.make(), 'RGB')
img.save('math_paint.png')
from random import randint

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

class Rectangle:
    
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

rectangle = Rectangle(Point(randint(0,9), randint(0,9)), Point(randint(10,19), randint(10,19)))

print("Rectangle coordinates: ", rectangle.lowleft.x, ",", rectangle.lowleft.y, "and", rectangle.upright.x, ",", rectangle.upright.y)
user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

print ("Your point was inside the rectangle: ", user_point.falls_in_rectangle(rectangle))
user_area = int(input ("Can you guess the area of the rectangle?: "))
if user_area == rectangle.area:
    print ("You guessed!!!")
else:
    print ("Not quite, the area of the rectangle is: ", rectangle.area())


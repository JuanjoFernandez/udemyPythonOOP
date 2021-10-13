class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def find_distance(self, point):
        distance = ( (self.x - point.x)**2 + (self.y - point.y)**2 )**0.5
        return distance

class Rectangle:
    
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

pointx = Point(6, 7)
rectanglex = Rectangle(Point(5, 6), Point(7, 9))

print(pointx.falls_in_rectangle(rectanglex))




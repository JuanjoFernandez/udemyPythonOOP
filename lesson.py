class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def find_distance(self, point):
        distance = ( (self.x - point.x)**2 + (self.y - point.y)**2 )**0.5
        return distance

point1 = Point(1, 1)
point2 = Point(2, 2)
print(point1.find_distance(point2))


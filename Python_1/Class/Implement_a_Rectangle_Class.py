# Problem Statement #
# Implement a class named Rectangle to store the coordinates of a rectangle given the top-left corner (x1, y1) and
# the bottom-right corner (x2, y2).
#
# Implement the class constructor with the parameters (x1, y1, x2, y2) and store them in the class instance using
# the self keyword.

# My solution
class Rectangle:
    # write your code here
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def output(self):
        if self.x1 < self.x2 and self.y1 > self.y2:
            return "Rectangle ({}, {}, {}, {} created)".format(self.x1, self.y1, self.x2, self.y2)


# Real solution
class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        if x1 < x2 and y1 > y2:
            self.x1 = x1  # class variable
            self.y1 = y1  # class variable
            self.x2 = x2  # class variable
            self.y2 = y2  # class variable
        else:
            print("Incorrect coordinates of the rectangle!")


r = Rectangle(2, 7, 8, 4)
# The code for the Rectangle class is implemented below:
#
# Create a Square class as a ​subclass of Rectangle.
#
# Implement the Square constructor. The constructor should have only the x1, y1 coordinates and the length of a side.
# Notice which arguments you’ll have to use when you invoke the Rectangle constructor while using super.
#
# The following test cases will calculate the area of the square to check that the Square class correctly inherits
# attributes and methods from Rectangle.

# My solution
class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        self.x1 = x1  # class variable
        self.y1 = y1  # class variable
        self.x2 = x2  # class variable
        self.y2 = y2  # class variable

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return self.width() * self.height()


class Square(Rectangle):
    # write your code here
    def __init__(self, x1, y1, lenght):
        x2 = x1 + lenght
        y2 = y1 + lenght
        super().__init__(x1, y1, x2, y2)

    def area(self):
        return super().areaa()


# Real solution
class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        self.x1 = x1  # class variable
        self.y1 = y1  # class variable
        self.x2 = x2  # class variable
        self.y2 = y2  # class variable

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return self.width() * self.height()


# write your code here
class Square(Rectangle):
    def __init__(self, x1, y1, length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1, y1, x2, y2)


# test your code here
square = Square(2, 7, 7)
print("Length: " + str(square.width()) + ", Area: " + str(square.area()))
square2 = Square(1, 3, 5)
print("Length: " + str(square2.width()) + ", Area: " + str(square2.area()))
print(x.batch)
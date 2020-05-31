# Problem Statement #
# Implement a function in the Rectangle class __str__ method, such that when you print one of the objects using
# the print() command, it prints the coordinates as x1, y1, x2, y2.

# Real solution
class Rectangle:
  def __init__(self, x1, y1, x2, y2): # class constructor
    self.x1 = x1 # class variable
    self.y1 = y1 # class variable
    self.x2 = x2 # class variable
    self.y2 = y2 # class variable
  #write your code here
  def __str__(self):
    return "{}, {}, {}, {}".format(self.x1, self.y1, self.x2, self.y2)


 # Real solution1
class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        if x1 < x2 and y1 > y2:
            self.x1 = x1  # class variable
            self.y1 = y1  # class variable
            self.x2 = x2  # class variable
            self.y2 = y2  # class variable
        else:
            print("Incorrect coordinates of the rectangle!")

    def __str__(self):
        return (str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', ' + str(self.y2))

    # test your code


r = Rectangle(2, 7, 8, 4)
print(r)

# Real solution 2
class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        if x1 < x2 and y1 > y2:
            self.x1 = x1  # class variable
            self.y1 = y1  # class variable
            self.x2 = x2  # class variable
            self.y2 = y2  # class variable
        else:
            print("Incorrect coordinates of the rectangle!")

    def __repr__(self):
        return (str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', ' + str(self.y2))


# test your code
r = Rectangle(2, 7, 8, 4)
print(r)
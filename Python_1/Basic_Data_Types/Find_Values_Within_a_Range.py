# Problem Statement #
# Given an inRange(x,y) function, write a method that determines whether a given pair (x, y) falls in the range
# (x < 1/3 < y). Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and
# returns True if x < 1/3 < y; otherwise, it returns False.Range

# My solution
def inRange(x, y):
  ## Write your code herean
  if x < 1/3 and y > 1/3:
    result = True
  else:
    result = False
  return result ## Change this to return True or return False depending on your output

# Real solution
def inRange(x, y):
  return (x < 1/3 < y)

print(inRange(-1, 3))
print(inRange(2, 3))
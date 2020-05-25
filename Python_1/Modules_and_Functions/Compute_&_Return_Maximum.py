# Problem Statement #
# Implement the findMaximum function that receives two numbers as arguments x and y and returns the maximum of
# the numbers.

# My solution
def findMaximum(x, y):
    return x if x > y else y


# Real solution 1
def findMaximum(x, y):
  max2 = 0
  if(x > y):
    max2 = x
  else:
    max2 = y
  return max2
print(findMaximum(3, 2))

# Real solution 2
def findMaximum(x, y):
  max2 = max(x, y)
  return max2
print(findMaximum(2, 3))
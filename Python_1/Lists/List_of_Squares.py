# Problem Statement #
# Given a getSquare() function, create a list with the squares of the first 10 numbers, i.e., in the range from 1-10.

# My solution
def getSquare():
  ## Write your code here
  l1 = [x**2 for x in range(1, 11)] ## Create your list here
  return l1


# Real solution
def getSquare():
  l1 = [x*x for x in range(1, 11)]
  return l1
l1 = getSquare()
print(l1)
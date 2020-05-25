# Problem Statement #
# Given a getCube() function, create a list with the cubes of the first 20 numbers.

# My solution
def getCube():
  ## Write your code here
  l1 = [x**3 for x in range(1, 21)] ## Make the list here
  return l1


# Real solution 1
def getCube():
  l1 = [x*x*x for x in range(1, 21)]
  return l1
l1 = getCube()
print(l1)

# Real solution 2
def getCube():
  l1 = [x**3 for x in range(1,21)]
  return l1

l1 = getCube()
print(l1)
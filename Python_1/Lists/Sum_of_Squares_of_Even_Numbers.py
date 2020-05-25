# Problem Statement #
# Given an evenSquare() function, create a list with the squares of the even numbers from 0 to 20. The final output
# should be the sum of even numbers in the list:

# My solution
def evenSquareSum():
  #write code here
  l1 = [x**2 for x in range(0, 21) if (x%2 == 0)]
  return sum(l1)


# Real solution
def evenSquareSum():
    even = [x * x for x in range(0, 21, 2)]
    return sum(even)


print(evenSquareSum())
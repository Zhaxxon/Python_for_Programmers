# Problem Statement #
# Given a checkParity(n) function, write code to determine if a given number n is even or odd. Think of this as
# a function that returns 0 if the number is even, and 1 if it is odd. You have been given some starter code where
# the function and return statement have already been written, so don’t worry about any Python-specific details
# about functions; just implement the function logic!

# My solution
def checkParity(n):
  ## Write your code here
  if n % 2 == 0:
    result = 0 ## Update result according to the parity
  else:
    result = 1
  return result


# Real solution
def checkParity(n):
  result = (n % 2)
  return result

print("Odd parity", checkParity(17))
print("Even parity", checkParity(16))
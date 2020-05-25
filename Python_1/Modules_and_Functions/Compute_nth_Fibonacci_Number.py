# Problem Statement #
# Implement the Fibonacci function that takes a number n and calculates the nth Fibonacci.
#
# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … The next number is found by
# adding up the previous two consecutive numbers.

# My solution
def fibonacci(n):
   if n == 1: ## write base case
      return 1
   elif n == 2:
      return 1
   else: ## write recursive case
      return (fibonacci(n - 1) + fibonacci(n - 2))


# Real solution
def fibonacci(n):
  if n <= 1:
       return n
  else:
       return(fibonacci(n-1) + fibonacci(n-2))
print(fibonacci(4))
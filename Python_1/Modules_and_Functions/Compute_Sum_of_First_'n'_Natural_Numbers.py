# Problem Statement #
# Implement a sum_N_Numbers recursive function to compute the sum of the n natural numbers (where (n) is a
# function parameter). Start by thinking about the base case (the sum of the first 1 integers is?) and then think about the recursive case.
#
# Note: Natural Numbers start from 1, i.e., 1, 2, 3, 4, 5, …

# My solution
def sum_N_Numbers (n):
  # Write code here
  if n == 1:
    return 1
  else:
    return (n + sum_N_Numbers(n-1))


# Real solution
def sum_N_Numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_N_Numbers(n - 1)


print(sum_N_Numbers(5))
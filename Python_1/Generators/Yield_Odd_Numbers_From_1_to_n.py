# Problem Statement #
# Create a generator to yield all the odd numbers from 1 to n.

# My solution
def odd(n):
  # write your code here
  for i in range(n+1):
    if i % 2 != 0:
      yield i


# Real solution
def odd(n):
  for value in range(n):
    if value % 2 is not 0:
      yield value

for j in odd(8):
  print(j)
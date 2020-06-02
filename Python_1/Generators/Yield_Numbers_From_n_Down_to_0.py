# Problem Statement #
# Implement a generator reverse(n) that returns All numbers from n down to 0.

# My solution
def reverse(n):
  # write your code here
  for i in range(n, -1, -1):
    yield i


# Real solution
def reverse(n):
  for value in range(n, -1, -1):
    yield value

for i in reverse(8):
  print(i)
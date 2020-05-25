# Problem Statement #
# Implement a function named isDivisible that receives two parameters (named x and y) and only returns true if “x”
# can be divided by “y”(and false otherwise).

# My solution
def isDivisble(x, y):
  # Write code here!
  return True if x % y == 0 else False


# Real solution
def isDivisble(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(isDivisble(24, 4))
print(isDivisble(24, 7))
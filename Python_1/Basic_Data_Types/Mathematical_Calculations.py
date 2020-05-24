# Problem Statement #

# Given a MathOp() function, try the following mathematical calculations and print the output:
# (3 / 2)
# (3 // 2)
# (3 % 2)
# (3**2)

# The expected output:
# 1.5
# 1
# 1
# 9

# My solution
def MathOp(a, b):
    print(a / b)
    print(a // b)
    print(a % b)
    print(a ** b)

# Real solution
def MathOp():
    classic_division = 3 / 2  ## Calculate 3/2 here
    floor_division = 3 // 2  ## Calculate 3//2 here
    modulus = 3 % 2  ## Calculate 3%2 here
    power = 3 ** 2  ## Calculate 3**2 here
    ## Returning the calculations for evaluation
    return [classic_division, floor_division, modulus, power]


[classic_division, floor_division, modulus, power] = MathOp()
print(classic_division)
print(floor_division)
print(modulus)
print(power)
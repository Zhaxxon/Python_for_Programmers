# Circular Imports
# a.py
import b

def a_test():
    print('in a test')
    b.b_test()

a_test()

# b.py
import a

def b_test():
    print('in b test')
    a.a_test()

# Shadowed Imports
import math

def square_root(number):
    return math.sqrt(number)

square_root(72)
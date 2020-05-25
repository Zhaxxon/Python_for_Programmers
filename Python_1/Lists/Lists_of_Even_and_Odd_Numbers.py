# Problem Statement #
# Given a ListofEvenOdds() function, create a list comprehension with all the even numbers from 0 to 20, and another
# one with all the odd numbers.

# My solution
def ListofEvenOdds():
  l1 = [x for x in range(21) if x % 2 == 0] # list of even numbers
  l2 = [x for x in range(21) if x % 2 == 1 ] # list of odd numbers
  return [l1, l2]


# Real solution1
def ListofEvenOdds():
    l1 = []
    l2 = []
    l1 = [x for x in range(0, 21) if (x % 2 == 0)]
    l2 = [x for x in range(0, 21) if (x % 2 != 0)]
    return [l1, l2]


print(ListofEvenOdds())

# My solution 2
def ListofEvenOdds():
    l1 = []
    l2 = []
    l1 = [x for x in range(0, 21) if (x % 2 == 0)]
    l2 = [x for x in range(0, 21) if (x not in l1)]
    return [l1, l2]


print(ListofEvenOdds())
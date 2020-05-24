# Problem Statement #
# Given an AppendtoList() function, create a list named l with the following values:
#
# [1, 4, 9, 10, 23]
#
# and appends the number 90 at the end of the list.

# My solution
def AppendtoList():
  l = [1, 4, 9, 10, 23]
  # Write your code here
  l.append(90)
  return l


# Real solution 1
def AppendtoList():
  l = [1, 4, 9, 10, 23]
  l.append(90)
  return l
l = AppendtoList()
print(l)

# Real solution 2
def AppendtoList():
    l1 = [1, 4, 9, 10, 23]
    print(l1)
    l1 = l1 + [90]
    print(l1)
# Problem Statement #
# Given a removeList() function, create a list named l with the following values:
#
# [1, 4, 9, 10, 23]
#
# Remove the sublist [4, 9] from list l

# My solution
def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  ## Write your code here
  l1.remove(l2[0])
  l1.remove(l2[1])
  return l1


# Real solution 1
def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  l1.remove(l2[0])
  l1.remove(l2[1])
  return l1

l1 = removeList()
print(l1)

# Real solution 2
def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    for elem in l2:
        l1.remove(elem)
    return l1


l1 = removeList()
print(l1)
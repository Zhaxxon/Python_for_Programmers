# Problem Statement #
# Given a getAverage() function, create a list named l with the following values:
#
# [1, 4, 9, 10, 23]
#
# Calculate the average value of all values in the list.

# My solution
def getAverage():
  l1 = [1, 4, 9, 10, 23]
  ## Write your code here
  avg = sum(l1) / len(l1) ## Calculate the average here
  return avg


# Real solution
def getAverage():
    l1 = [1, 4, 9, 10, 23]
    avg = sum(l1) / len(l1)
    return avg


avg = getAverage()
print(avg)
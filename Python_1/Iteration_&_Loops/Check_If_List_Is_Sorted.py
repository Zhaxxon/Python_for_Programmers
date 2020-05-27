# Problem Statement #
# Make an isSorted function that receives a list as a ​parameter and returns true if the list is sorted
# in ascending order.
#
# For instance, [1, 2, 2, 3] is ordered while [1, 2, 3, 2] is not.

# My solution
def isSorted(list):
  # write your code here
  for i in range(len(list)):
    if list[i] <= list[i+1]:
      return True
    else:
      return False


# Real solution
def isSorted(list):
    flag = 0
    i = 1
    while i < len(list):
        if (list[i] < list[i - 1]):  # compare with the previous element
            flag = 1
        i += 1

    if (not flag):
        return True
    else:
        return False


print(isSorted([1, 2, 3, 4, 5]))
print(isSorted([1, 2, 5, 4, 2]))
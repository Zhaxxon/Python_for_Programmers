# Problem Statement #
# Implement a reverse function that receives a list as a parameter and returns the reverse of that list. You may
# create an empty list and keep adding the values in reversed order as they come from the original list.


# My solution
def reverse(list):
  # Write your code here
  new_list = []
  for i in reversed(range(len(list))):
    new_list.append(list[i])
  return new_list


# Real solution
def reverse(list):
    length = len(list)
    s = length

    new_list = [None] * length

    for item in list:
        s = s - 1
        new_list[s] = item
    return new_list


list = [1, 2, 3, 4, 5]
print(reverse(list))
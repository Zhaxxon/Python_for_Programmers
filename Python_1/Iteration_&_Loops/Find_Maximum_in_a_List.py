# Problem Statement 1 #
# Create a findMaximum function that receives a list as a parameter and returns the maximum value in the list.
# As you iterate over the list, you may want to keep track of the current maximum value in order to keep comparing
# it with the next elements of the list.

# My solutuion

def findMaximum(list):
    # write your code here
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        else:
            max = max
    return max


# Real solution
def findMaximum(list):
    maximum = list[0]
    for x in list:
        if x > maximum:
            maximum = x
    return maximum


list = [1, 2, 7, 4, 5]

print(findMaximum(list))


# Problem Statement 2 #
# Modify the previous findMaximumValueIndex(list) function such that it returns a list with the first element being
# the index of the maximum value in the list and the second being the maximum value. Besides keeping the maximum
# value found so far, you also need to keep the position where it occurred.

# My solution
def findMaximumValueIndex(list):
    # write your code here
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        else:
            max = max
    return [i, max]


# Real solution
def findMaximumValueIndex(list):
    maximum = list[0]
    index = 0
    for i, value in enumerate(list):
        if value > maximum:
          maximum = value
          index = i
    return [index, maximum]

list = [1, 2, 7, 4, 5]
[index, maximum] = findMaximumValueIndex(list)

print("Index:", index)
print("Maximum Value:", maximum)

print(findMaximumValueIndex(list))
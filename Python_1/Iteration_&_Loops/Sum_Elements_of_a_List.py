# Problem Statement #
# Create a sumList function that receives a list as a parameter and returns the sum of all the elements in the list.

# My solution
def sumList(l):
    sum = 0
    for elem in l:
        sum += elem
    return sum


# Real solution
def sumList(l):
    sum = 0
    for x in l:
        sum += x
    return sum
l = [1, 2, 3, 4, 5]
print(sumList(l))
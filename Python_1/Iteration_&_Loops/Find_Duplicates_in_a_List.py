# Problem Statement #
# Implement the hasDuplicates function which verifies if a list has duplicate values.

# My solution
def hasDuplicates(list):
    # write code here
    count = 1

    for i in range(len(list)):
        value = list.count(list[i])
        if value > 1:
            count += 1
        else:
            count = count

    if count > 1:
        return True
    else:
        return False


# Real solution
def has_duplicates(list):
    flag = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i] == list[j]):
                flag = 1
    if (flag == 1):
        return True
    else:
        return False


l = [1, 2, 3, 4, 5]
print(has_duplicates(l))
l = [1, 2, 3, 3, 4]
print(has_duplicates(l))
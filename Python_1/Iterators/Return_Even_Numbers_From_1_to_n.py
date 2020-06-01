# Problem Statement #
# Edit the following iterator class to return all the positive even numbers from 1 to (n). The following test cases
# will test your code using
#
# myrange = MyRange(n) # n is an integer
# print(myrange.next())

# My solution
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        even_num = []
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                even_num.append(i)
        return even_num


myrange = MyRange(8)
print(myrange.next())


# Real solution
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        evenArray = []  # next method returns this list
        for i in range(1, self.n + 1):
            if i % 2 is 0:  # checks if number is even
                value = i
                evenArray.append(i)  # adds the even number to the list
            else:  # number was odd
                i += 1
        return evenArray


myrange = MyRange(8)
print(myrange.next())
# Problem Statement #
# Edit the following iterator class to return the Fibonacci sequence from the first element up to the nth element.
#
# The Fibonacci Sequence is the series of numbers in which the next term is found by adding the two previous terms:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Here , the number 0 is the first term, 1 is the second term, 1 is the third term and so on…

# My solution
class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    #write your code here
    fibonacci_num = []
    for i in range(self.n):
      if i <= 1:
        fibonacci_num.append(i)
      else:
        fibonacci_num.append(fibonacci_num[i-1] + fibonacci_num[i-2])
    return fibonacci_num


# Real solution
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        myArray = []
        for i in range(self.n):  # from n to 0
            if i == 0 or i == 1:
                myArray.append(i)  # adds the even number to the list
            else:
                myArray.append(myArray[i - 2] + myArray[i - 1])
        return myArray


myrange = MyRange(8)
print(myrange.next())
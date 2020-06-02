# Problem Statement #
# Create a generator to return the Fibonacci sequence starting from the first element up to n.


# My solution
def fibonacci(n):
  # write your code here
  fibonacci_num = []
  for i in range(n):
    if i <= 1:
      fibonacci_num.append(i)
      yield i
    else:
      fibonacci_num_2 = fibonacci_num[i-1] + fibonacci_num[i-2]
      fibonacci_num.append(fibonacci_num_2)
      yield fibonacci_num_2


# Real solution
def fibonacci(n):
    myArray = []
    for i in range(n):
        if i is 0 or i is 1:
            myArray.append(i)
            yield i
        else:
            x = myArray[i - 2] + myArray[i - 1]
            myArray.append(x)
            yield x


for i in fibonacci(8):
    print(i)
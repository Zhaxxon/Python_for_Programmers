# Problem Statement #
# Implement a printEvenOdd function that receives a number n as parameter and prints–in decreasing order–which numbers
# are even and which are odd until it reaches 0. For instance, on calling printEvenOdd(10) it prints

def printEvenOdd(n):
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print("Even number: ", i)
        else:
            print("Odd number: ", i)


# Real solution
def printEvenOdd(n):
    while (n > 0):
        if (n % 2 == 0):
            print("Even number:", n)
        else:
            print("Odd number", n)
        n -= 1

printEvenOdd(10)
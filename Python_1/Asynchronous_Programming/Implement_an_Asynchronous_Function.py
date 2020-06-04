# Problem Statement #
# Implement an asynchronous coroutine function to add two variables and sleep for the duration of the sum. Use the
# asyncio loop to call the function with two numbers.
#
# Input #
# Two number n1 and n2
#
# Output #
# The sum of two numbers
#
# Sample Input #
# n1 = 1, n2 = 2
#
# Sample Output #
# 3

# My solution
import asyncio

async def sum(n1, n2):
    await asyncio.sleep(n1 + n2)
    return n1 + n2

loop = asyncio.get_event_loop() # Create event loop

results = loop.run_until_complete(sum(1, 2)) # Run async function and wait for completion
print(results)

loop.close() # Close the loop


# Real solution
import asyncio

async def sum(n1,n2):
    print('Sum numbers', n1, '+', n2)
    await asyncio.sleep(1)
    print('End Sum', n1, '+', n2)
    return n1 + n2

# Create event loop
loop = asyncio.get_event_loop()
n1 = 1
n2 = 2
# Run async function and wait for completion
results = loop.run_until_complete(sum(n1, n2))
print("Sum of two numbers:", n1, "+", n2, "=", results)

# Close the loop
loop.close()
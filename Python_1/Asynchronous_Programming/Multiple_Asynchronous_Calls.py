# Problem Statement #
# Change the previous program to schedule the execution of two calls to the sum function.
#
# Input #
# Two number n1 and n2
#
# Output #
# The sum of two numbers in the order of the execution.

# My solution
import asyncio

async def sum(n1,n2):
    print('Sum numbers',n1,'+',n2)
    await asyncio.sleep(1)
    print('End Sum',n1,'+',n2)
    return n1 + n2

# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
    sum(1, 2),
    sum(2, 3),
    sum(3, 4)
))
print(results)

# Close the loop
loop.close()


# Real solution
import asyncio

async def sum(n1, n2):
    print('Sum numbers', n1, '+', n2)
    await asyncio.sleep(1)
    print('End Sum', n1, '+', n2)
    return n1 + n2

# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
    sum(1, 2),
    sum(2, 3),
    sum(3, 4)
))
print(results)

# Close the loop
loop.close()
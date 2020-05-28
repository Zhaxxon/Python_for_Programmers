# Problem Statement #
# # Implement a calculateAvg function that receives the ages dictionary as a ​parameter, and returns the average age of
# # the students. Traverse all items in the dictionary using the “items” method above.

# My solution
def calculateAvg(ages):
  sum = 0
  for key, value in ages.items():
    sum += value
  avg = sum / len(ages)
  return avg # return the average of ages


# Real solution
def calculateAvg(ages):
  length=len(ages)
  return(sum(ages.values())/length)
ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
 }
print(calculateAvg(ages))
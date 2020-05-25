# Problem Statement #
# Use the calculateSinCosTan() function; it takes a number x as a parameter and shows the result of the sine,
# cosine, and tangent of the number.

# My solution
import math
def calculateSinCosTan(x):
  #write your function here
  sine = math.sin(x) #calculate sine
  cos = math.cos(x) #calculate cosine
  tan = math.tan(x) #calculate tangent
  return [sine, cos, tan]


# Real solution
import math
def calculateSinCosTan(x):
  sine = math.sin(x)
  cos = math.cos(x)
  tan = math.tan(x)
  return [sine, cos, tan]

print("sine:", calculateSinCosTan(-1))
print("cos:", calculateSinCosTan(0))
print("tan:", calculateSinCosTan(1))
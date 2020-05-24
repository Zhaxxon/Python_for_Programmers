# Problem Statement #
# Given a string, use a findOccurence(s) function that allows you to find the first occurrences of "b" and
# "ccc"​ in the string.

# My solution
def findOccurence(s):
  # Write your code here
  a = s.find('b') #find first occurrence of "b" in the string
  b = s.find('c') #find first occurence  of "ccc" in the string
  return [a, b]


# Real solution
def findOccurence(s):
  a = s.find("b")#find first occurrence of "b" in the string
  b = s.find("ccc")#find first occurence  of "ccc" in the string
  return [a, b]

str = "aaabbccc"
print(findOccurence(str))
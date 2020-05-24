# Problem Statement #
# Given a function changeCase(s), the task is to convert the strings from upper case to lower case.

# My solution
def changeCase(s):
    # Write your code here
    a = s.upper() # convert string to "AAA BBB CCC"
    b = s.lower() # convert string to "aaa bbb ccc"
    return [a, b]


# Real solution
def changeCase(s):
  a = s.upper()  # convert string to "AAA BBB CCC"
  b = s.lower()  # convert string to "aaa bbb ccc"
  return [a, b]

str = "AAA bbb CCC"
print(changeCase(str))
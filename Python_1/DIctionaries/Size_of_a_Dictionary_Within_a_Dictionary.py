# Problem Statement​ #
# Given a totalStudents function, your task is to calculate how many students are in the students dictionary.

# My solution
def totalStudents(students):
  # write your code here
  num = 0
  for key in students:
    num += 1
  return num # return the number of students in the dictionary


# Real solution 1
def totalStudents(students):
  return(len(students.keys()))

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
print(totalStudents(students))

# Real solution 2
def totalStudents(students):
  return len(students)

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
print(totalStudents(students))
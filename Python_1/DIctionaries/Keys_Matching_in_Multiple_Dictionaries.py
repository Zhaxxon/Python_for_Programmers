# Problem Statement #
# Implement a find_students function that receives the students dictionary and an address, and returns a list with
# names of all students whose address matches the address in the argument. For instance, invoking find_students
# ('Lisbon') should return Anna and Peter. Also, note that the names should be printed in alphabetical order.

# My solution
def find_students(address, students):
  # Write code here
  output = []
  for key, value in students.items():
    if address == value['address']:
      output.append(key)
  return sorted(output)


# Real solution 1
def find_students(address, students):
  names = []
  for key, subdict in students.items():
       for sublist in subdict.values():
          if (sublist == address):
             names.append(key)
  return sorted(names)

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
print(find_students("Lisbon", students))

# Real solution 2
def find_students(address, students):
  names = []
  for key, value in students.items():
    if value["address"] == address:
      names.append(key)
  return sorted(names)

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
print(find_students("Lisbon", students))
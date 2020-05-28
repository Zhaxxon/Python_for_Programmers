# Problem Statement #
# Implement an oldestStudent function that receives the ages dictionary as a parameter, and returns the name of the
# oldest student.

# My solution
def oldesStudent(ages):
    oldest = max(ages.values())
    for key, value in ages.items():
        if value == oldest:
            return key


#  Real solution
def oldestStudent(ages):
    value = list(ages.values())
    key = list(ages.keys())
    return key[value.index(max(value))]


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
print(oldestStudent(ages))
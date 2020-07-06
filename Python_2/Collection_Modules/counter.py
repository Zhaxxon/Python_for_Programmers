from collections import Counter
print(Counter('superfluous'))

counter = Counter('superfluous')
print(counter['u'])

print(list(counter.elements()))

print(counter.most_common(2))

counter_one = Counter('superfluous')
print(counter_one)

counter_two = Counter('super')
print(counter_one.subtract(counter_two))

print(counter_one)
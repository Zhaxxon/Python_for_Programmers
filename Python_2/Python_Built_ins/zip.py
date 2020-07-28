keys = ['x', 'y', 'z']
values = [5, 6, 7]
print(zip(keys, values))
# <zip object at 0x7faaad4dd848>

print(list(zip(keys, values)))
# [('x', 5), ('y', 6), ('z', 7)]


keys = ['x', 'y', 'z']
values = [5, 6, 7]
my_dict = dict(zip(keys, values))
print (my_dict)
#{'x': 5, 'y': 6, 'z': 7}
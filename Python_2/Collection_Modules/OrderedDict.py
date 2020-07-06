d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print (d)
#{'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}

keys = d.keys()
print(keys)

keys = sorted(keys)
print(keys)

for key in keys:
    print(key, d[key])

from collections import OrderedDict
new_d = OrderedDict(sorted(d.items()))
print(new_d)

for key in new_d:
    print(key, new_d[key])

for key in reversed(new_d):
    print(key, new_d[key])
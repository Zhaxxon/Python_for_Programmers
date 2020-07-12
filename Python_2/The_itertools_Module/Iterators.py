# count(start=0, step=1)
from itertools import count

for i in count(5):
    if i > 20:
        break
    else:
        print(i)

#10
#11
#12
#13
#14
#15
#16
#17
#18
#19
#20

from itertools import islice

for i in islice(count(10), 5):
    print(i)

#10
#11
#12
#13
#14

# cycle(iterable)
from itertools import cycle
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1

#X
#Y
#Z
#X
#Y
#Z
#X
#Y

polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)
print (next(iterator))
#'triangle'

print (next(iterator))
#'square'

print (next(iterator))
#'pentagon'

print (next(iterator))
#'rectangle'

print (next(iterator))
#'triangle'

print (next(iterator))
#'square'

# repeat(object)
from itertools import repeat
repeat(5, 5)
repeat(5, 5)

iterator = repeat(5, 5)
print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 21, in <module>
# print (next(iterator))
#StopIteration:
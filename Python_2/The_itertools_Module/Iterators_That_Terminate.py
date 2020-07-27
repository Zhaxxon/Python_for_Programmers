# accumulate(iterable)
from itertools import accumulate
print(list(accumulate(range(10))))
#[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

import operator
print(list(accumulate(range(1, 5), operator.mul)))
#[1, 2, 6, 24]


# chain(*iterables)
my_list = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list.extend(cmd, numbers)
my_list
#['foo', 'bar', ['ls', '/some/dir'], [0, 1, 2, 3, 4]]

#Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 4, in <module>
# my_list.extend(cmd, numbers)
#TypeError: extend() takes exactly one argument (2 given)

from itertools import chain
my = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list = list(chain(['foo', 'bar'], cmd, numbers))

print(my_list)
#['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]


# chain.from_iterable(iterable)
from itertools import chain
numbers = list(range(5))
cmd = ['ls', '/some/dir']
print (chain.from_iterable(cmd, numbers))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 4, in <module>
# print (chain.from_iterable(cmd, numbers))
#TypeError: from_iterable() takes exactly one argument (2 given)

from itertools import chain
numbers = list(range(5))
cmd = ['ls', '/some/dir']

print (list(chain.from_iterable([cmd, numbers])))
#['ls', '/some/dir', 0, 1, 2, 3, 4]


# compress(data, selectors)
from itertools import compress
letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print(list(compress(letters, bools)))
#['A', 'C', 'D']


# dropwhile(predicate, iterable)
from itertools import dropwhile
print (list(dropwhile(lambda x: x<5, [1,4,6,4,1])))
#[6, 4, 1]

from itertools import dropwhile
def greater_than_five(x):
    return x > 5

print (list(dropwhile(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
#[1, 2, 3, 10]


# filterfalse(predicate, iterable)
from itertools import filterfalse
def greater_than_five(x):
    return x > 5

print (list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
#[1, 2, 3]


# groupby(iterable, key=None)
from itertools import groupby

vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]

sorted_vehicles = sorted(vehicles)

for key, group in groupby(sorted_vehicles, lambda make: make[0]):
    for make, model in group:
        print('{model} is made by {make}'.format(model=model,
                                                 make=make))
    print ("**** END OF GROUP ***\n")
# Cobalt is made by Chevrolet
# **** END OF GROUP ***
#
# Charger is made by Dodge
# Durango is made by Dodge
# **** END OF GROUP ***
#
# F150 is made by Ford
# GT is made by Ford


# islice(iterable, start, stop)
from itertools import islice
iterator = islice('123456', 4)
print (next(iterator))
#'1'

print (next(iterator))
#'2'

print (next(iterator))
#'3'

print (next(iterator))
#'4'

print (next(iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 15, in <module>
# print (next(iterator))
#StopIteration:

from itertools import islice
from itertools import count
for i in islice(count(), 3, 15):
    print(i)
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12
#13
#14


# starmap(function, iterable)
from itertools import starmap
def add(a, b):
    return a+b

for item in starmap(add, [(2,3), (4,5)]):
    print(item)
#5
#9


# takewhile(predicate, iterable)
from itertools import takewhile
print (list(takewhile(lambda x: x<5, [1,4,6,4,1])))
#[1, 4]


# tee(iterable, n=2)
from itertools import tee
data = 'ABCDE'
iter1, iter2 = tee(data)
for item in iter1:
    print(item)
#A
#B
#C
#D
#E

for item in iter2:
    print(item)
#A
#B
#C
#D
#E


# zip_longest(*iterables, fillvalue=None)
from itertools import zip_longest
for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
    print (item)

#('A', 'x')
#('B', 'y')
#('C', 'BLANK')
#('D', 'BLANK')
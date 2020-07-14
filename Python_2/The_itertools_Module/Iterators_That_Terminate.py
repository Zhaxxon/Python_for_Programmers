# accumulate(iterable)
from itertools import accumulate
print(list(accumulate(range(10))))

import operator
print(list(accumulate(range(1, 5), operator.mul)))

# chain(*iterables)
from itertools import chain
my = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']
my_list = list(chain(['foo', 'bar'], cmd, numbers))

print(my_list)

# chain.from_iterable(iterable)
print(chain.from_iterable([cmd, numbers]))
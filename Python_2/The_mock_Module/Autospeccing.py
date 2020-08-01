from unittest.mock import create_autospec
def add(a, b):
    return a + b

mocked_func = create_autospec(add, return_value=10)
print (mocked_func(1, 2))
#10

mocked_func(1, 2, 3)
#Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 9, in <module>
# mocked_func(1, 2, 3)
# File "<string>", line 2, in add
# File "/usr/lib/python3.5/unittest/mock.py", line 183, in checksig
# sig.bind(*args, **kwargs)
# File "/usr/lib/python3.5/inspect.py", line 2918, in bind
# return args[0]._bind(args[1:], kwargs)
# File "/usr/lib/python3.5/inspect.py", line 2839, in _bind
# raise TypeError('too many positional arguments') from None
#TypeError: too many positional arguments
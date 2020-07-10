from functools import singledispatch
#
# @singledispatch
# def add(a, b):
#     raise NotImplementedError('Unsupported type')
#
# @add.register(int)
# def _(a, b):
#     print('First argument is of type ', type(a))
#     print(a+b)
#
# @add.register(str)
# def _(a, b):
#     print('First argument is of type ', type(a))
#     print(a+b)
#
# @add.register(list)
# def _(a, b):
#     print('First argument is of type ', type(a))
#     print(a+b)
#
# if __name__ == '__main__':
#     add(1, 2)
#     add('Python', 'Programming')
#     add([1, 2, 3], [5, 6, 7])
#
# print(add.registry.keys())

from decimal import Decimal

@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')

@add.register(float)
@add.register(Decimal)
def _(a, b):
    print('First argument is of type ', type(a))
    print(a+b)

if __name__ == '__main__':
    add(1.23, 5.5)
    add(Decimal(100.5), Decimal(10.789))
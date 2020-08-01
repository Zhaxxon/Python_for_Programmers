"""
print(list(range(100))) # doctest: +ELLIPSIS
#[0, 1, ..., 98, 99]

class Dog: pass
Dog() #doctest: +ELLIPSIS
#<__main__.Dog object at 0x...>
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
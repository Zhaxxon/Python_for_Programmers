class X:
    def __init__(self):
        print('X')
        super().__init__()

class Y:
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)
# X
# Y
# (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)


class Base:
    var = 5
    def __init__(self):
        pass

class X(Base):
    def __init__(self):
        print('X')
        super().__init__()

class Y(Base):
    var = 10
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)
print(super(Z, z).var)
# X
# Y
# (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Base'>, <class 'object'>)
# 10


class Base():
    def __init__(self):
        s = super()
        print(s.__thisclass__)
        print(s.__self_class__)
        s.__init__()

class SubClass(Base):
    pass

sub = SubClass()
# <class '__main__.Base'>
# <class '__main__.SubClass'>
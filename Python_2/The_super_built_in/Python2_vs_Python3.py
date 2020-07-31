# Python2
class MyParentClass(object):
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        MyParentClass.__init__(self)

class SubClass(MyParentClass):
    def __init__(self):
        super(SubClass, self).__init__()


# Python3
class MyParentClass():
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        super().__init__()

class MyParentClass():
    def __init__(self, x, y):
        pass

class SubClass(MyParentClass):
    def __init__(self, x, y):
        super().__init__(x, y)
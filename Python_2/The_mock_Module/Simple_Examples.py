from unittest.mock import Mock
my_mock = Mock()
my_mock.__str__ = Mock(return_value='Mocking')
print(str(my_mock))
#'Mocking'


from unittest.mock import Mock
class TestClass():
    pass

cls = TestClass()
cls.method = Mock(return_value='mocking is fun')
print (cls.method(1, 2, 3))
#'mocking is fun'

cls.method.assert_called_once_with(1, 2, 3)
print (cls.method(1, 2, 3))
#'mocking is fun'


from unittest.mock import Mock
class TestClass():
    pass

cls = TestClass()
cls.method = Mock(return_value='mocking is fun')
cls.method(1, 2, 3)
#'mocking is fun'

cls.method.assert_called_once_with(1, 2, 3)
cls.method(1, 2, 3)
#'mocking is fun'

cls.method.assert_called_once_with(1, 2, 3)
#Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 14, in <module>
# cls.method.assert_called_once_with(1, 2, 3)
# File "/usr/lib/python3.5/unittest/mock.py", line 804, in assert_called_once_with
# raise AssertionError(msg)
# AssertionError: Expected 'mock' to be called once. Called 2 times.

cls.other_method = Mock(return_value='Something else')
cls.other_method.assert_not_called()
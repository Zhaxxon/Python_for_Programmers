x = 10
def my_func(a, b):
    print(x)
    print(z)

my_func(1, 2)
#10
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 7, in <module>
#    my_func(1, 2)
#  File "/usercode/__ed_file.py", line 4, in my_func
#    print(z)
#NameError: name 'z' is not defined


def my_func(a, b):
    i = 2
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(i)
# 10
# Traceback (most recent call last):
#   File "main.py", line 8, in <module>
#     print(i)
# NameError: name 'i' is not defined


def my_func(a, b):
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(x)
# 5
# 10


def my_func(a, b):
    print(x)
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(x)
# Traceback (most recent call last):
#   File "main.py", line 8, in <module>
#     my_func(1, 2)
#   File "main.py", line 2, in my_func
#     print(x)
# UnboundLocalError: local variable 'x' referenced before assignment
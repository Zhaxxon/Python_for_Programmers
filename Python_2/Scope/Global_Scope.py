def my_func(a, b):
    global x
    print(x)
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(x)
# 10
# 5
# 5


def my_func(a, b):
    global c
    # swap a and b
    b, a = a, b
    d = 'Mike'
    print(a, b, c, d)

a, b, c, d = 1, 2, 'c is global', 4
my_func(1, 2)
print(a, b, c, d)
# 2 1 c is global Mike
# 1 2 c is global 4
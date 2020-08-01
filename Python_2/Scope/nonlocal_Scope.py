def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter()

print(c)
# <function counter.<locals>.incrementer at 0x7f78918f3378>

print(c())
# 1

print(c())
# 2

print(c())
# 3

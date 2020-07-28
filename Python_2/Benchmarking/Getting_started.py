# simple_func.py
def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass

# python -m timeit "import simple_func; simple_func.my_function()" 1000000 loops, best of 3: 1.77 usec per loop
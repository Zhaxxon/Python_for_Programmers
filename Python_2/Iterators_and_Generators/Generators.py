# Simple generator
def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number

doubler = doubler_generator()
print(next(doubler))
# 2

print(next(doubler))
# 4

print(next(doubler))
# 16

print(type(doubler))

def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"
gen = silly_generator()
print (next(gen))
#'Python'

print (next(gen))
#'Rocks'

print (next(gen))
#'So do you!'

# print (next(gen))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 15, in <module>
# print (next(gen))
#StopIteration:

for item in gen:
    print(item)
from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)

d.append('bork')
# print(d)

d.appendleft('test')
# print(d)

d.rotate(1)
print(d)

def get_last(filename, n=5):
    """
    Returns the last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print('Error opening file: {}'.format(filename))
        raise
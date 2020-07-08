# Before
import sys

path = 'text.txt'

with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)

# With context module
from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)
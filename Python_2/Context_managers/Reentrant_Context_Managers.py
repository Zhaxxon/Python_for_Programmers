from contextlib import contextmanager
@contextmanager
def single():
    print('Yielding')
    yield
    print('Exiting context manager')
context = single()
with context:
    pass

#Yielding
#Exiting context manager

with context:
    pass

#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 14, in <module>
# with context
#  File "/usr/local/lib/python3.5/contextlib.py", line 61, in __enter__
#    raise RuntimeError("generator didn't yield") from None
#RuntimeError: generator didn't yield

from contextlib import redirect_stdout
from io import StringIO
stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
    print('Write something to the stream')
    with write_to_stream:
        print('Write something else to stream')

print(stream.getvalue())
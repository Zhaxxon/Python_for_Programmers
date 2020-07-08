with open('fauxfile.txt') as fobj:
    for line in fobj:
        print(line)

#Traceback (most recent call last):
#   File "/usercode/__ed_file.py", line 1, in <module>
# with open('fauxfile.txt') as fobj:
#FileNotFoundError: [Errno 2] No such file or directory: 'fauxfile.txt''

# To ignore the following above we use the below code
from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

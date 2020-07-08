from contextlib import contextmanager

@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()

from urllib.request import urlopen

with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass
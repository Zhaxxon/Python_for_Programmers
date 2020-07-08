from contextlib import ExitStack
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename)) for filename in filenames]
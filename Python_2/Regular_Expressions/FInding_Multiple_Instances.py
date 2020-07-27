import re
silly_string = "the cat in the hat"
pattern = "the"
match = re.search(pattern, silly_string)
print (match.group())
#'the'

import re
silly_string = "the cat in the hat"
pattern = "the"
print (re.findall(pattern, silly_string))
#['the', 'the']

import re

silly_string = "the cat in the hat"
pattern = "the"

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    print(s)
# Found 'the' at 0:3
# Found 'the' at 11:14
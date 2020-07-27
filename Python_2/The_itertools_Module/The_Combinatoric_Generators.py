# combinations(iterable, r)
from itertools import combinations
print (list(combinations('WXYZ', 2)))
#[('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]

from itertools import combinations
for item in combinations('WXYZ', 2):
    print(''.join(item))
#WX
#WY
#WZ
#XY
#XZ
#YZ


# combinations_with_replacement(iterable, r)
from itertools import combinations_with_replacement
for item in combinations_with_replacement('WXYZ', 2):
    print(''.join(item))
#WW
#WX
#WY
#WZ
#XX
#XY
#XZ
#YY
#YZ
#ZZ


# product(*iterables, repeat=1)
from itertools import product
arrays = [(-1,1), (-3,3), (-5,5)]
cp = list(product(*arrays))
print (cp)
#[(-1, -3, -5),
# (-1, -3, 5),
# (-1, 3, -5),
# (-1, 3, 5),
# (1, -3, -5),
# (1, -3, 5),
# (1, 3, -5),
# (1, 3, 5)]


# permutations
from itertools import permutations
for item in permutations('WXYZ', 2):
    print(''.join(item))
#WX
#WY
#WZ
#XW
#XY
#XZ
#YW
#YX
#YZ
#ZW
#ZX
#ZY
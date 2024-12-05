import re
from functools import cmp_to_key

def ints(iterable):
    return [int(x) for x in re.findall(r'[-]?\d+', iterable)]

def compare(a, b):
    if (a, b) in adj: return -1
    if (b, a) in adj: return 1
    return 0

adj, queries = [x.strip().split('\n') for x in open(0).read().split('\n\n')]
adj = {tuple(ints(x)) for x in adj}

res = [0, 0]
for q in queries:
    a = ints(q)
    b = sorted(a, key=cmp_to_key(compare))
    res[a != b] += b[len(b) // 2]

print(*res, sep='\n')

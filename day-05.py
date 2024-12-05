import re
from functools import cmp_to_key

def ints(iterable):
    return [int(x) for x in re.findall(r'[-]?\d+', iterable)]

adj, queries = [[ints(y) for y in x.split()] for x in open(0).read().split('\n\n')]
adj = {tuple(x) for x in adj}

key = cmp_to_key(lambda a, b: ((b, a) in adj) - ((a, b) in adj))

print(sum(b[len(b)//2] for a in queries if a == (b:= sorted(a, key=key))))
print(sum(b[len(b)//2] for a in queries if a != (b:= sorted(a, key=key))))

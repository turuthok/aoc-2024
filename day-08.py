arr = [x.strip() for x in open(0)]
rows, cols = len(arr), len(arr[0])
inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

from collections import defaultdict
from itertools import combinations
from math import gcd

antennas = defaultdict(list)
for i in range(rows):
    for j in range(cols):
        if arr[i][j] != '.':
            antennas[arr[i][j]].append((i, j))

def calc(part):
    res = set()

    for coords in antennas.values():
        for (a, b), (c, d) in combinations(coords, 2):
            di = c-a; dj = d-b

            if part == 1:
                if inbound(*(p := (a-di, b-dj))): res.add(p)
                if inbound(*(p := (c+di, d+dj))): res.add(p)
            else:
                g = gcd(abs(di), abs(dj))
                di //= g; dj //= g

                i, j = a, b
                while inbound(i, j):
                    res.add((i, j))
                    i += di; j += dj

                i, j = a, b
                while inbound(i, j):
                    res.add((i, j))
                    i -= di; j -= dj

    return len(res)

print(calc(1))
print(calc(2))


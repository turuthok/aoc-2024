arr = [x.strip() for x in open(0)]
rows, cols = len(arr), len(arr[0])
inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

from collections import defaultdict

antennas = defaultdict(list)
for i in range(rows):
    for j in range(cols):
        if arr[i][j] != '.':
            antennas[arr[i][j]].append((i, j))

def calc(part):
    res = set()

    for coords in antennas.values():
        for (a, b) in coords:
            for (c, d) in coords:
                if (a, b) == (c, d): continue
                di = c-a; dj = d-b

                if part == 1:
                    if inbound(*(p := (a-di, b-dj))): res.add(p)
                else:
                    i, j = a, b
                    while inbound(i, j):
                        res.add((i, j))
                        i += di; j += dj

    return len(res)

print(calc(1))
print(calc(2))


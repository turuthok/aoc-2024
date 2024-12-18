arr = [[int(y) for y in x.split(",")] for x in open(0)]
R = C = 71

def bfs(s, t, n):
    g = [['.'] * C for _ in range(R)]
    for x, y in arr[:n]: g[y][x] = '#'

    q = [s]
    seen = {s: 0}
    for x, y in q:
        if (x, y) == t: return seen[(x, y)]
        for xx, yy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if xx < 0 or xx >= C or yy < 0 or yy >= R: continue
            if g[yy][xx] == '#': continue
            if (xx, yy) in seen: continue
            seen[(xx, yy)] = seen[(x, y)] + 1
            q.append((xx, yy))
    return -1

print(bfs((0, 0), (R-1, C-1), 1024))

lo, hi = 0, len(arr)
while lo+1 < hi:
    m = (lo+hi) // 2
    if bfs((0, 0), (R-1, C-1), m) >= 0:
        lo = m
    else:
        hi = m
print(*arr[lo], sep=',')
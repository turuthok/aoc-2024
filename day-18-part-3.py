from collections import deque

arr = [[int(y) for y in x.split(",")] for x in open(0)]
R = C = 71

g = [['.'] * C for _ in range(R)]
for x, y in arr: g[y][x] = '#'

def bfs(s, t):
    q = deque()

    q.append(s)
    seen = {s: 0}
    while q:
        x, y = q.popleft()
        if (x, y) == t: return seen[(x, y)]
        for xx, yy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if xx < 0 or xx >= C or yy < 0 or yy >= R: continue
            if (xx, yy) in seen: continue
            if g[yy][xx] == '.':
                seen[(xx, yy)] = seen[(x, y)]
                q.appendleft((xx, yy))
            else:
                seen[(xx, yy)] = seen[(x, y)] + 1
                q.append((xx, yy))
    return -1

print(bfs((0, 0), (R-1, C-1)))
from collections import defaultdict

arr = [x.strip() for x in open(0)]
R, C = len(arr), len(arr[0])
TOP, RIGHT, BOTTOM, LEFT = 1, 2, 4, 8
DY, DX, DIR = [-1, 0, 1, 0], [0, 1, 0, -1], [TOP, RIGHT, BOTTOM, LEFT]
valid = lambda i, j: 0 <= i < R and 0 <= j < C

visited = [[False] * C for _ in range(R)]

def fill(i, j, char):
    if not valid(i, j) or visited[i][j] or arr[i][j] != char: return set()
    visited[i][j] = True
    res = {(i, j)}
    for dy, dx in zip(DY, DX):
        res |= fill(i+dy, j+dx, char)
    return res

INF = 1_000_000

def calc_perimeter(cells):
    l, r, t, b = INF, -INF, INF, -INF
    data = defaultdict(int)
    perimeter = 0
    for (i, j) in cells:
        l = min(l, j); r = max(r, j)
        t = min(t, i); b = max(b, i)
        for dy, dx, d in zip(DY, DX, DIR):
            if (i+dy, j+dx) not in cells:
                data[(i, j)] |= d
                perimeter += 1

    sides = 0
    for j in range(l, r+1):
        ll = rr = 0
        for i in range(t, b+1):
            if data[(i, j)] & LEFT:
                if ll == 0:
                    sides += 1
                    ll = 1
            else:
                ll = 0

            if data[(i, j)] & RIGHT:
                if rr == 0:
                    sides += 1
                    rr = 1
            else:
                rr = 0
    for i in range(t, b+1):
        bb = tt = 0
        for j in range(l, r+1):
            if data[(i, j)] & TOP:
                if tt == 0:
                    sides += 1
                    tt = 1
            else:
                tt = 0
            if data[(i, j)] & BOTTOM:
                if bb == 0:
                    sides += 1
                    bb = 1
            else:
                bb = 0
    return perimeter, sides

def gen():
    for i in range(R):
        for j in range(C):
            if visited[i][j]: continue
            cells = fill(i, j, arr[i][j])
            perimeter, sides = calc_perimeter(cells)
            yield len(cells), perimeter, sides

data = list(gen())
print(sum(a * b for a, b, _ in data))
print(sum(a * c for a, _, c in data))

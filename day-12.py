from collections import defaultdict

arr = [x.strip() for x in open(0)]
R, C = len(arr), len(arr[0])
DY, DX = [-1, 0, 1, 0], [0, 1, 0, -1]
valid = lambda i, j: 0 <= i < R and 0 <= j < C

v = [[False] * C for _ in range(R)]

def flood_fill(r, c, char):
    if not valid(r, c) or v[r][c] or arr[r][c] != char: return set()
    v[r][c] = True
    res = {(r, c)}
    for dy, dx in zip(DY, DX):
        res |= flood_fill(r+dy, c+dx, char)
    return res

def trace_sides(e):
    last = (-1, -1)
    res = 0
    for a, b in sorted(e):
        if a != last[0] or b != last[1]+1: res += 1
        last = (a, b)
    return res

def calc_perimeter_and_sides(cells):
    perimeter = 0
    edges = defaultdict(list)
    for r, c in cells:
        for d, (dy, dx) in enumerate(zip(DY, DX)):
            rr = r+dy; cc = c+dx
            if (rr, cc) not in cells:
                perimeter += 1
                if d & 1:
                    edges[d].append((c, r))
                else:
                    edges[d].append((r, c))
    return perimeter, sum(trace_sides(e) for e in edges.values())

def gen():
    for i in range(R):
        for j in range(C):
            if v[i][j]: continue
            cells = flood_fill(i, j, arr[i][j])
            perimeter, sides = calc_perimeter_and_sides(cells)
            yield len(cells), perimeter, sides

data = list(gen())
print(sum(a * b for a, b, _ in data))
print(sum(a * c for a, _, c in data))

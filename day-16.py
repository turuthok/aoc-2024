import heapq

arr = [x.strip() for x in open(0)]
R, C = len(arr), len(arr[0])
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INF = 1_000_000_000

def find_cell(char):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == char: return (i, j)

def relax(cost, si, sj, sd, d, dist):
    if (si, sj, sd) not in dist or cost < dist[(si, sj, sd)]:
        dist[(si, sj, sd)] = cost
        heapq.heappush(d, (cost, si, sj, sd))

def dijkstra(si, sj, sd):
    dist = {(si, sj, sd): 0}
    d = [(0, si, sj, sd)]
    while d:
        cost, si, sj, sd = heapq.heappop(d)
        if cost > dist[(si, sj, sd)]: continue
        relax(cost+1000, si, sj, (sd+1) % 4, d, dist)
        relax(cost+1000, si, sj, (sd+3) % 4, d, dist)
        dy, dx = DIR[sd]
        if arr[si+dy][sj+dx] != '#':
            relax(cost+1, si+dy, sj+dx, sd, d, dist)
    return dist

(si, sj), sd = find_cell('S'), 1
from_s = dijkstra(si, sj, sd)

ei, ej = find_cell('E')
best = min(from_s[(ei, ej, x)] for x in range(4))
print(best)

from_e = [dijkstra(ei, ej, x) for x in range(4)]
cells = set()
for i in range(R):
    for j in range(C):
        if arr[i][j] == '#': continue
        for direction in range(4):
            cost = from_s[(i, j, direction)] + min(x[i, j, (direction + 2) % 4] for x in from_e)
            if cost == best:
                cells.add((i, j))
                break
print(len(cells))

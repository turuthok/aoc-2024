import heapq

arr = [x.strip() for x in open(0)]
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_cell(char):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
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

si, sj = find_cell('S')
from_s = dijkstra(si, sj, 1)

ei, ej = find_cell('E')
best = min(from_s[(ei, ej, x)] for x in range(4))
print(best)

cells = {(ei, ej)}
def go(ei, ej, ed, expected_cost):
    if (ei, ej, ed) not in from_s or from_s[(ei, ej, ed)] != expected_cost: return
    cells.add((ei, ej))

    dy, dx = DIR[ed]
    go(ei-dy, ej-dx, ed, expected_cost-1)
    go(ei, ej, (ed+1) % 4, expected_cost-1000)
    go(ei, ej, (ed+3) % 4, expected_cost-1000)

for ed in range(4): go(ei, ej, ed, best)
print(len(cells))

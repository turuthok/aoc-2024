arr = [x.strip() for x in open(0)]
R, C = len(arr), len(arr[0])
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
valid = lambda i, j: 0 <= i < R and 0 <= j < C

def bfs(i, j):
    q = [(i, j)]
    seen = {(i, j): 0}
    for i, j in q:
        for dy, dx in D:
            ii, jj = i+dy, j+dx
            if not valid(ii, jj): continue
            if arr[ii][jj] == '#': continue
            if (ii, jj) in seen: continue
            q.append((ii, jj))
            seen[(ii, jj)] = seen[(i, j)] + 1
    return seen

find_char = lambda ch: [(i, j) for i in range(R) for j in range(C) if arr[i][j] == ch][0]

si, sj = find_char('S')
ei, ej = find_char('E')
a = bfs(si, sj)
b = bfs(ei, ej)

no_cheat_cost = a[(ei, ej)]

def cheat(n):
    res = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '#': continue
            for dy in range(-n, n+1):
                rem = n - abs(dy)
                for dx in range(-rem, rem+1):
                    ii, jj = i + dy, j + dx
                    if not valid(ii, jj): continue
                    if arr[ii][jj] == '#': continue
                    d = abs(dy) + abs(dx)
                    if no_cheat_cost - (a[(i, j)] + b[(ii, jj)] + d) >= 100:
                        res += 1
    return res

print(cheat(2))
print(cheat(20))

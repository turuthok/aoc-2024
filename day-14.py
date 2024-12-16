import math, re

ints = lambda iterable: list(int(x) for x in re.findall(r'[-]?\d+', iterable))

def points_at(sx, sy, vx, vy, t):
    return (sx + t * vx) % C, (sy + t * vy) % R

arr = [ints(x) for x in open(0)]
R, C = 103, 101
quads = [0] * 4
for info in arr:
    x, y = points_at(*info, 100)
    if y == R // 2 or x == C // 2: continue
    q = (y < R // 2) + 2 * (x < C // 2)
    quads[q] += 1
print(math.prod(quads))

t = 0
while True:
    t += 1
    s = {points_at(*info, t) for info in arr}
    if len(s) == len(arr): break
print(t)

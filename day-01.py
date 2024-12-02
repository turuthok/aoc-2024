from collections import Counter

def transpose_ccw(arr):
    return [list(a) for a in zip(*arr)][::-1]

a, b = transpose_ccw([[int(x) for x in line.split()] for line in open(0)])
print(sum(abs(x-y) for x, y in zip(sorted(a), sorted(b))))

c = Counter(b)
print(sum(c[x] * x for x in a))
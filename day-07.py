import re

ints = lambda iterable: list(int(x) for x in re.findall(r'[-]?\d+', iterable))

arr = [ints(x) for x in open(0)]

def calc(base, arr):
    tgt, first, *x = arr
    n = len(x)

    def go(i, val):
        if val > tgt: return False
        if i == n: return tgt == val
        for op in range(base):
            if op == 0 and go(i+1, val * x[i]): return True
            if op == 1 and go(i+1, val + x[i]): return True
            if op == 2 and go(i+1, int(f"{val}{x[i]}")): return True
        return False

    return tgt if go(0, first) else 0

print(sum(calc(2, x) for x in arr))
print(sum(calc(3, x) for x in arr))

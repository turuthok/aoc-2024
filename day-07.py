import re

ints = lambda iterable: list(int(x) for x in re.findall(r'[-]?\d+', iterable))

arr = [x.strip() for x in open(0)]

def calc(base, arr):
    tgt, *x = arr
    n = len(x) - 1
    for idx in range(base ** n):
        res = x[0]
        for i in range(n):
            d = idx % base
            idx //= base
            if d == 0:
                res *= x[i+1]
            elif d == 1:
                res += x[i+1]
            else:
                res = int(str(res) + str(x[i+1]))
        if tgt == res:
            return tgt
    return 0

print(sum(calc(2, ints(x)) for x in arr))
print(sum(calc(3, ints(x)) for x in arr))

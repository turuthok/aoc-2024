import re

ints = lambda s: list(int(x) for x in re.findall(r'\d+', s))

arr = [x.strip().split('\n') for x in open(0).read().split('\n\n')]

def calc(section, additional):
    a, b, c = section
    ax, ay = ints(a)
    bx, by = ints(b)
    cx, cy = (x + additional for x in ints(c))

    num = cx * ay - cy * ax
    den = bx * ay - by * ax
    if num % den == 0:
        B = num // den
        num = cx - B * bx
        if num % ax == 0:
            A = num // ax
            return A * 3 + B

    return 0

print(sum(calc(x, 0) for x in arr))
print(sum(calc(x, 10000000000000) for x in arr))

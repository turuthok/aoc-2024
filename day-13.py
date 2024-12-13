import re

ints = lambda s: list(int(x) for x in re.findall(r'\d+', s))

arr = [x.strip().split('\n') for x in open(0).read().split('\n\n')]

def calc(section, extra=0):
    a, b, c = section
    ax, ay = ints(a)
    bx, by = ints(b)
    cx, cy = (x + extra for x in ints(c))

    # A ax + B bx = cx ... * ay
    # A ay + B by = cy ... * ax
    # -- try removing A
    # A ax ay + B bx ay = cx ay
    # A ax ay + B by ax = cy ax
    # ------------------------- -
    # B (bx ay - by ax) = (cx ay - cy ax)
    # B = (cx ay - cy ax) / (bx ay - by ax)
    #
    # Make sure numerator evenly divides denominator.
    # Resolve A, make sure it's not negative
    # Resolve B, make sure it's not negative
  
    num = cx * ay - cy * ax
    den = bx * ay - by * ax
    if num % den == 0:
        B = num // den
        num = cx - B * bx
        if num % ax == 0:
            A = num // ax
            if A >= 0 and B >= 0:
                return A * 3 + B

    return 0

print(sum(calc(x) for x in arr))
print(sum(calc(x, 10000000000000) for x in arr))

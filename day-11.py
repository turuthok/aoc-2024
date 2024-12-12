from functools import cache

@cache
def go(x, steps):
    if steps == 0: return 1
    if x == 0: return go(1, steps-1)
    s = str(x)
    if (l := len(s)) & 1:
        return go(2024 * x, steps-1)
    else:
        return sum(go(num, steps-1) for num in divmod(x, 10 ** (l >> 1)))

arr = [int(x) for x in input().split()]

print(sum(go(x, 25) for x in arr))
print(sum(go(x, 75) for x in arr))

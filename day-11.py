from functools import cache

@cache
def go(x, n):
    if n == 0: return 1
    if x == 0: return go(1, n-1)
    s = str(x)
    if (l := len(s)) % 2 == 0:
        l //= 2
        return go(int(s[:l]), n-1) + go(int(s[l:]), n-1)
    return go(2024 * x, n-1)

arr = [int(x) for x in input().split()]

print(sum(go(x, 25) for x in arr))
print(sum(go(x, 75) for x in arr))

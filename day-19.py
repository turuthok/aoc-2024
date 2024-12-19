from functools import cache

a, b = [x.strip().split('\n') for x in open(0).read().split('\n\n')]
a = a[0].split(", ")

@cache
def go(s):
    return 1 if not s else sum(go(s[len(x):]) for x in a if s.startswith(x))

print(sum(go(x) != 0 for x in b))
print(sum(go(x) for x in b))
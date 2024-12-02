def is_increasing(x):
    return all(1 <= x[i+1]-x[i] <= 3 for i in range(len(x)-1))

def is_safe(x):
    return is_increasing(x) or is_increasing(x[::-1])

arr = [[int(x) for x in line.split()] for line in open(0)]

print(sum(map(is_safe, arr)))
print(sum(any(is_safe(x[:i] + x[i+1:]) for i in range(len(x))) for x in arr))
s = input()

arr = []
free = []
block_id = 0
disk = []
for i, repeat in enumerate(map(int, s)):
    pos = len(disk)
    next_pos = pos + repeat
    if pos == next_pos: continue

    if i % 2 == 0:
        arr.append([pos, next_pos, block_id])
        for p in range(pos, next_pos): disk.append(block_id)
        block_id += 1
    else:
        free.append([pos, next_pos])
        for p in range(pos, next_pos): disk.append(-1)

# Part 1
l, r = 0, len(disk)-1
res = 0
while l <= r:
    while l < r and disk[l] >= 0:
        res += l * disk[l]
        l += 1
    while r >= l and disk[r] < 0:
        r -= 1
    if l > r: break

    res += l * disk[r]
    l += 1; r -= 1
print(res)

# Part 2    
for l, r, block_id in arr[::-1]:
    for i, (fl, fr) in enumerate(free):
        if fl >= l: break
        if fr-fl >= r-l:
            next_pos = fl + r-l
            for p in range(fl, next_pos):
                disk[p] = block_id
            free[i][0] = next_pos
            for p in range(l, r):
                disk[p] = -1
            break
print(sum(l * block_id for l, block_id in enumerate(disk) if block_id >= 0))

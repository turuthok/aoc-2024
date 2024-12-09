import heapq

s = input()

arr = []
free = [[] for _ in range(10)]
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
        heapq.heappush(free[repeat], pos)
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
    length = r-l
    free_slots = [(x, free[x]) for x in range(length, 10) if free[x]]
    if not free_slots: continue
    free_slot_length, free_slot = min(((x, slot) for x, slot in free_slots), key=lambda x: x[1][0])
    fl = free_slot[0]
    if fl < l:
        fl = heapq.heappop(free_slot)
        for p in range(fl, fl + length):
            disk[p] = block_id
        for p in range(l, r):
            disk[p] = -1
        if length < free_slot_length:
            heapq.heappush(free[free_slot_length-length], fl+length)

print(sum(l * block_id for l, block_id in enumerate(disk) if block_id >= 0))

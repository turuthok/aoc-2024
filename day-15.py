from itertools import chain

grid, moves = (x.strip().split('\n') for x in open(0).read().split('\n\n'))
arr = [[x for x in row] for row in grid]
moves = ''.join(moves)

DY, DX, ARROWS = [-1, 0, 1, 0], [0, 1, 0, -1], "^>v<"

def move(i, j, dy, dx):
    if arr[i][j] == '#': return False
    if arr[i][j] == '.': return True
    if move(i + dy, j + dx, dy, dx):
        arr[i + dy][j + dx] = arr[i][j]
        arr[i][j] = '.'
        return True
    return False

def move_vert_2(i, j, dy, dx, move_it=False):
    if arr[i][j] == '#': return False
    if arr[i][j] == '.': return True
    off = ']['.find(arr[i][j]) * 2 - 1

    if move_vert_2(i + dy, j, dy, dx, move_it) and move_vert_2(i + dy, j+off, dy, dx, move_it):
        if move_it:
            arr[i + dy][j] = arr[i][j]
            arr[i + dy][j+off] = arr[i][j+off]
            arr[i][j] = '.'; arr[i][j+off] = '.'
        return True

    return False

def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '@':
                arr[i][j] = '.'
                return i, j

def solve(arr, part):
    i, j = find_start(arr)

    for m in moves:
        d = ARROWS.find(m)
        dy, dx = DY[d], DX[d]
        if part == 1:
            if move(i + dy, j + dx, dy, dx):
                i += dy; j += dx
        else:
            if m in "<>":
                if move(i + dy, j + dx, dy, dx):
                    i += dy; j += dx
            else:
                if move_vert_2(i + dy, j + dx, dy, dx):
                    move_vert_2(i + dy, j + dx, dy, dx, True)
                    i += dy; j += dx

    return sum(i * 100 + j for i in range(len(arr)) for j in range(len(arr[0])) if arr[i][j] in '[O')

print(solve(arr, 1))

arr = [list(chain.from_iterable('[]' if x == 'O' else '@.' if x == '@' else x * 2 for x in row)) for row in grid]
print(solve(arr, 2))


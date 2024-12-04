arr = [x.strip() for x in open(0)]
rows, cols = len(arr), len(arr[0])

def search(word):
    n = len(word)
    for i in range(rows):
        for j in range(cols):
            for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if 0 <= i + (n-1) * di < rows and 0 <= j + (n-1) * dj < cols:
                    if word == ''.join(arr[i + k * di][j + k * dj] for k in range(n)):
                        yield (i, j, di, dj)

print(len(list(search('XMAS'))))

coords = [(i+di, j+dj) for i, j, di, dj in search('MAS') if di != 0 and dj != 0]
print(len(coords) - len(set(coords)))

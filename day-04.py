arr = [x.strip() for x in open(0)]
rows, cols = len(arr), len(arr[0])
inbound = lambda i, j: 0 <= i < rows and 0 <= j < cols

def search(word):
    for i in range(rows):
        for j in range(cols):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (di, dj) == (0, 0): continue
                    s, ii, jj = '', i, j
                    for _ in range(len(word)):
                        if not inbound(ii, jj): break
                        s += arr[ii][jj]
                        ii += di; jj += dj
                    else:
                        if s == word:
                            yield (i, j, di, dj)


print(len(list(search('XMAS'))))

coords = [(i+di, j+dj) for i, j, di, dj in search('MAS') if di != 0 and dj != 0]
print(len(coords) - len(set(coords)))


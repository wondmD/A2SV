from collections import defaultdict
n,m = map(int, input().split())

grid = []
for l in range(n):
    grid.append(list(input()))

rows = [defaultdict(int) for i in range(n)]
cols = [defaultdict(int) for i in range(n)]

for i in range(n):
    for j in range(m):
        rows[i][grid[i][j]] += 1
        cols[j][grid[i][j]] += 1

result = []
for i in range(n):
    for j in range(m):
        if rows[i][grid[i][j]] == 1 and cols[j][grid[i][j]] == 1:
            result.append(grid[i][j])

print(''.join(result))
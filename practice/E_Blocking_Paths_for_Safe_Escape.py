from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    n, m= map(int, stdin.readline().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, stdin.readline().split())))
    directions = [(0,1),[0,-1],(-1,0),(1,0)]
    # print(grid)
    def inbound(row, col):
        return 0 <= row < n and 0<=col < m
    good_idx = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for direction in directions:
                    if inbound(i+direction[0], j+direction[1]):
                        if grid[i+direction[0]][j+direction[1]] == 'G':
                            return 'NO'
                        elif grid[i+direction[0]][j+direction[1]] == '':
                            grid[i+direction[0]][j+direction[1]] = '#'
            
            elif grid[i][j] == 'G':
                good_idx.append((i,j))
    q = deque([good_idx])
    while q:
        i, j = q.popleft()
        for direction in directions:
            
            pass

# 


# jjkkn









        # print "


for _ in range(int(input())):
    print(sol())

from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    x, y, X, Y = map(int, stdin.readline().split())
    x1 = min(x,y)
    y1 = max(x,y)
    x2 = min(X,Y)
    y2 = max(X,Y)
    if not (x1 <= x2 <= y1 or x1 <= y2 <= y1) or not (x2 <= x1 <= y2 or x2 <= y1 <= y2) :
        return 'NO'
    return 'YES' 

for _ in range(int(input())):
    print(sol())

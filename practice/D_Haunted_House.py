from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    s = stdin.readline()
    map = []
    for i in range(num):
        if s[i] == '0':
            map.append(num-i-1)
    map.reverse()
    for i in range(len(map)):
        map[i] -= i
        if i >=1:
            map[i] = map[i] + map[i-1]
    # return map
    for i in range(num-len(map)):
        map.append(-1)
    ans = []
    return(map)

for _ in range(int(input())):
    print(*sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    s = stdin.readline().strip()
    c =0
    for i in range(num-1, -1,-1):
        if s[i] == ')':
            c +=1
            if c > num/2:
                return 'Yes'
        else:
            return 'No'
    return 'Yes'

for _ in range(int(input())):
    print(sol())
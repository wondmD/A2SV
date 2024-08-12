from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    
    odd = 0
    even = 0
    for i in lis:
        if i %2 :
            odd += 1
        else:
            even += 1
    if odd == even:
        return "Yes"
    return 'No'


for _ in range(int(input())):
    print(sol())

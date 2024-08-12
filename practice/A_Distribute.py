from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    lis2 = [(lis[i],i+1) for i in range(num)]
    lis2.sort()
    # print(lis2)
    for i in range(num//2):
        print(lis2[i][1], lis2[num-1-i][1])

# for _ in range(int(input())):
sol()
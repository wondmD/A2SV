from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from math import ceil


def sol():
    num = int(stdin.readline())
    lis1 = list(map(int, stdin.readline().split()))
    lis2 = list(map(int, stdin.readline().split()))

    number_of_shoots = 0
    base = lis1[0]
    for i in range(1,num):
        shoot_needed = ceil(lis1[i]/lis2[i-1])
        


for _ in range(int(input())):
    print(sol())
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    ans = arr[0]
    for i in arr:
        ans&=i
    return ans
    # bits = [True for _ in range(32)]
    # for i in arr:
    #     p = 0
    #     while i > 0:
    #         if 1&i == 0:
    #             bits[p] = False
    #         i >>= 1
    #         p+=1
    # min_ = min(arr)
    # leng = len(bin(min_))-2
    # ans = 0
    # for i in range(leng):
    #     if bits[i]:
    #         ans += 2**i
    # return ans
for _ in range(int(input())):
    print(sol())
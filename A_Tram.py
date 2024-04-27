from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

def sol():
    res = 0
    ans = 0
    for _ in range(int(input())):
        a, b= map(int, stdin.readline().split())
        res += b-a
        ans = max(ans, res)
    return ans


print(sol())
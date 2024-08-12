from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
def sol():
    n, m = map(int, stdin.readline().split())
    a = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        a.append(row)
    ans = -1
    for i in range(n):
        for j in range(m):
            sum_val = 0
            for k, l in zip(range(i, n), range(j, m)):
                sum_val += a[k][l]
            for k, l in zip(range(i, n), range(j, -1, -1)):
                sum_val += a[k][l]
            for k, l in zip(range(i, -1, -1), range(j, m)):
                sum_val += a[k][l]
            for k, l in zip(range(i, -1, -1), range(j, -1, -1)):
                sum_val += a[k][l]
            sum_val -= 3 * a[i][j]
            ans = max(ans, sum_val)test.py
    return ans
for _ in range(int(stdin.readline())):
    print(sol())
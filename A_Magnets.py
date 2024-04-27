from sys import stdin
# from collections import defaultdict, deque
# from bisect import bisect_left, bisect_right

num = int(stdin.readline())
group = 1
prev = input()
for _ in range(num-1):
    mag = input()
    if mag != prev:
        group += 1
        prev = mag
print(group)
from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    
    ans = [i for i in range(num, 0, -1)]
    # print(ans)
    if num%2:
        mid = num//2
        ans[mid], ans[mid+1] = ans[mid+1], ans[mid]
    return ans
    


for _ in range(int(input())):
    print(*sol())

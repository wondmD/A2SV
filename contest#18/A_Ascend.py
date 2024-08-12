from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))

   
    stack = []
    ans = 1
    for i in lis:
        if not stack:
            stack.append(i)
        elif stack[-1] < i:
            stack.append(i)
        else:
            ans = max(ans, len(stack))
            stack = [i]
    ans = max(ans, len(stack))
        
    return ans

# for _ in range(int(input())):
print(sol())

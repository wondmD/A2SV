from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    ans = []

    for i in range(num):
        rew = ''
        for j in range(num):
            if i%2 ==0:
                if j%2:
                    rew += '..'
                else:
                    rew += '##'
            else:
                if j%2 == 0:
                    rew += '..'
                else:
                    rew += '##'
        ans.append(rew)
        ans.append(rew)
    return '\n'.join(ans)


for _ in range(int(input())):
    print(sol())
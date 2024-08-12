from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    num = int(stdin.readline())
    s = stdin.readline().strip()
    ones = s.count('1')
    # print(ones)
    if ones ==2:
        # print('dsds')
        for i in range(num-1):
            if s[i] == '1' and s[i+1] == '1':
                return 'NO'
    if ones%2:
        return 'NO'
    

    return 'YES'
            
for _ in range(int(input())):
    print(sol())
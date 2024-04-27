from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def check(s):
    ss = str(s)
    if ss.count('1') + ss.count('0') == len(ss):
        return True
    return False
def sol():
    num = int(stdin.readline())
    if check(num):
        return 'YES'
    while not check(num) and num %10 == 0:
        num //=10
    s = str(num)
    if check(num) or s == s[::-1]:
        return 'YES'
    return 'NO'

    
        


for _ in range(int(input())):
    print(sol())
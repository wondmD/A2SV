from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

num = int(stdin.readline())
ans = 0 
ans += num//100
num -= (num//100)*100
# print(num)
ans += num//20
num -= (num//20)*20
ans += num//10
num -= (num//10)*10
ans += num//5
num -= (num//5)*5
ans += num//1
num -= (num//1)*1
print(ans)
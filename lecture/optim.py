from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


nums = [1,2,3,1]
memo = {}
#start from index 0
#if I rob index 0 i am going to rob index 2
#if I Didnt rob index 0 i am going to tob index 1
#our state is house index
#our base case is when our index is out of bound
leng = len(nums)
def robber(idx):
    if idx >= leng:
        return 0
    if idx not in memo:
        memo[idx] = max(robber(idx+1), robber(idx+2) + nums[idx])
    return memo[idx]

  
print(robber(0))



import math
def solution():
    
    n, k = map(int, input().split())
    demand = list(map(int, input().split()))
    supp = list(map(int, input().split()))

    tothrs = sum(supp)
    if tothrs > k:
        return -1
    left = 1
    right = max(demand)
    mid = 0
    ans = -1
    while (left <= right):
        mid = (left + right)//2
        tot = 0
        hrs = 0
        for i in range(n):
            val = math.ceil(demand[i]/mid)
            tot += val
            hrs += val * supp[i]
        if hrs <= k:
            right = mid - 1
            ans = mid
        else:
            left = mid+1
    return ans
for _ in range(int(input())):
    print(solution())

# print(solution())
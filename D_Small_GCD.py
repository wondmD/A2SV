import math

def sol():
    n = int(input())
    lis = list(map(int, input().split()))
    ans = 0
    lis.sort()
    for i in range(n-2):
        for j in range(i+1, n-1):
            ans += (math.gcd(lis[i], lis[j])) * (n-j-1)
    return ans
for _ in range(int(input())):
    print(sol())
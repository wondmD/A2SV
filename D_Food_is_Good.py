from sys import stdin
input = stdin.readline
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0] * (n+1)
    tot = 0
    pos = 1
    for i in range(n):
        tot += a[i]
        prefix[pos] = tot
        pos += 1
    low = 0
    for i in range(1, n):
        wanted = prefix[i] - tot
        if wanted >= low:
            return "NO"

        low = min(low, prefix[i])
    low = prefix[1]
    for i in range(2, n+1):
        wanted = prefix[i] =tot
        
        if wanted >= low:
            return "NO"
        low = min(low, prefix[i])
    return "YES"
for _ in range(int(input())):
    print(solution())

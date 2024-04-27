import math

# Precalculation
def lcm(a, b):
    return a // math.gcd(a, b) * b

# Solution Start Here
def solve():
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    ans = 0
    for i in range(k):
        if s[i] == 'W':
            cnt += 1
    ans = cnt
    for i in range(k, n):
        if s[i] == 'W':
            cnt += 1
        if s[i - k] == 'W':
            cnt -= 1
        ans = min(ans, cnt)
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

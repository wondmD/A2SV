import math


YES = ["YES", "Yes", "yes"]
NO = ["NO", "No", "no"]
MOD = {"i": 10**9 + 7, "l": 10**9 + 7}
INF = {"i": float('inf'), "l": float('inf')}

def Nsum(n):
    return (n * (n + 1)) // 2

def uround(a, b):
    return int((a * 1.0) / b + 0.5)

def pow2(p):
    return 1 << p

def main():
    t = int(input())
    while t:
        t -= 1
        n, k = map(int, input().split())
        mn, mx = INF["i"], -INF["i"]
        a = []
        for i in range(n):
            ai, bi = map(int, input().split())
            mn = min(mn, ai)
            mx = max(mx, bi)
            a.append((ai, bi))
        cnt = 0
        for ai, bi in a:
            if ai <= k <= bi:
                cnt += 1
        flag = False
        for i in range(mn, mx + 1):
            c = 0
            for aj, bj in a:
                if i != k and aj <= i <= bj and k <= bj and k >= aj:
                    c += 1
            if c >= cnt:
                flag = True
                break
        print(NO[0] if flag else YES[0])

if __name__ == "__main__":
    main()
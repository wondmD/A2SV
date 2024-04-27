import sys
input  = sys.stdin.readline


orda = ord('a')

for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = [0] * 26

    for i in range(n):
        cnt[ord(s[i]) - orda] += 1

    mx = max(cnt)

    print(max(2 * mx - n, n % 2))
    



from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    l = list(map(int,stdin.readline().split()))
    s = stdin.readline()
    tot = 1
    for i in range(n):
        tot *= l[i]
    if tot == 0:
        res = [0]*n
        print(*res)
        continue

    left = 0
    right = n-1
    res = []

    for i in range(n):
        res.append(tot%m)
        if s[i] == "L":
            tot //= l[left]
            left += 1
        else:
            tot //= l[right]
            right -= 1
    print(*res)


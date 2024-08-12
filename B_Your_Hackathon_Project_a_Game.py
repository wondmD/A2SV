from typing import List

def sol():
    n, m = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    c = [0] * (n + 1)

    for i in range(2, n + 1):
        if a[i - 1] > a[i]:
            b[i] = b[i - 1] + a[i - 1] - a[i]
        else:
            b[i] = b[i - 1]

    for i in range(n-1, 0, -1):
        if a[i + 1] > a[i]:
            c[i] = c[i + 1] + a[i + 1] - a[i]
        else:
            c[i] = c[i + 1]

    for _ in range(m):
        s, t = map(int, input().split())
        if s < t:
            print(b[t] - b[s])
        else:
            print(c[t] - c[s])

sol()
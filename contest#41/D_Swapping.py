def sol():
    n, x , m = map(int, input().split())
    left = x
    right = x
    for i in range(m):
        l, r = map(int, input().split())
        if l <left and r >= left :
            left = l
        if r > right and l <= right:
            right = r
    return right - left +1
for _ in range(int(input())):
    print(sol())

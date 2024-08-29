def sol():
    a,b, d = map(int,input().split())
    if a>d:
        return d
    mod = d-b%d
    return mod + b
for i in range(int(input())):
    print(sol())
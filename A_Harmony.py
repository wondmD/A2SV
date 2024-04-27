from sys import stdin
def sol():
    n,  x = map(int, stdin.readline().split())
    a = list(map(int,stdin.readline().split()))
    b = list(map(int,stdin.readline().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        if a[i] + b[i] > x:
            return "No"
    return 'Yes'

for _  in range(int(input())):
    print(sol())
    stdin.readline()
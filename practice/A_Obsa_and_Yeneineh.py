def sol():
    n = int(input())
    l = list(map(int, input().split()))
    t = int(input())
    for i in range(n-1):
        for j in range(i+1, n):
            if l[i]+l[j] == t:
                return 'YES'
    return 'NO'
print(sol())
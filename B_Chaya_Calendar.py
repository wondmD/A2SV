for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(1,n):
        c = l[i]
        while l[i] <= l[i-1]:
            l[i] += c
    print(l[-1])
            
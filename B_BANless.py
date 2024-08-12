t = int(input())
while t:
    t -= 1
    n = int(input())
    print((n+1)//2)
    i, j = 1, 3*n
    while i < j:
        print(i, j)
        i += 3
        j -= 3
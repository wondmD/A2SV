from math import ceil
for _ in range(int(input())):
    n , q = map(int, input().split())
    l = list(map(int, input().split()))
    x = len(set(l))  
    for __ in range(q):
        ll, r = map(int, input().split())
        diff = r+1 - ll
        y = len(set(l[ll:r+1]))
        val = 0
        if diff<=3 and diff%2:
            yay = ceil(diff/2) +1
        else:
            yay = ceil(diff/2)
        if  y > yay:
            print ('YES')
        else:
            print ('NO')
    
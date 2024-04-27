t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    inv_a = {i: 0 for i in range(1, n+1)}
    inv_b = {i: 0 for i in range(1, n+1)}
    
    for i in range(n):
        inv_a[a[i]] = i
        inv_b[b[i]] = i
    
    inv_count_a = sum(inv_a.values())
    inv_count_b = sum(inv_b.values())
    
    if inv_count_a > inv_count_b:
        a, b = b, a
    
    a.sort()
    b.sort(reverse=True)
    
    print(' '.join(map(str, a)))
    print(' '.join(map(str, b)))

    
def sol():
    n = int(input())
    l = list(map(int, input().split()))
    avg = sum(l) / n
    cur = 0
    for i in range(n):
        if l[i] > avg:
            cur += l[i]- avg
        elif l[i] < avg:
            cur -= avg - l[i]
        else:
            continue
        if cur < 0:
            
            return "NO"
    return 'YES'
    


for _ in range(int(input())):
    print (sol())
    
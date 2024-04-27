n, k, q = map(int, input().split())
t = list(map(int, input().split()))
displayed = set()

for _ in range(q):
    type, a = map(int, input().split())
    
    if type == 1:
        displayed.add(a)
        if len(displayed) > k:
            worst = min(displayed, key=lambda x: t[x-1])
            displayed.remove(worst)
    else:
        if a in displayed:
            print("YES")
        else:
            print("NO")



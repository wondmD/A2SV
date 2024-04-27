from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = sorted(l)
    if l == x or len(l) == 1:
        print(0)
        continue
    min_ = x[0]
    b = l.index(min_)
    let = l[ b:]
    let2 = sorted(let)
    if let != let2:
        print(-1)
        continue
    print(b)

    

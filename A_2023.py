for _ in range(int(input())):
    n,k = map(int, input().split())
    b = list(map(int, input().split()))
    _sum = 1
    for i in b:
        _sum *= i
    if 2023 % _sum != 0 :
        print ("NO")
    else:
        r = 2023/_sum
        ans = []
        for i in range(k-1):
            ans.append(1)
        ans.append(int(r))
        print('YES')
        print(*ans)
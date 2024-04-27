def solution():
    #solution here
    # n = int(input())
    # l = list(map(int, input().split()))

    n, h = map(int, input().split())
    res = 0
    for _ in range(n):
        a, b = map(int, input().split())
        res += max(a,b)

    if res >= h:
        return('YES')
    return ('NO')


for _ in range(int(input())):
    print(solution())

# print(solution())
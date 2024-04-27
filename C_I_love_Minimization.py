import itertools
t = int(input())

for tc in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    r = list(itertools.accumulate(r))
    b = list(itertools.accumulate(b))

    result = max(0, max(r)) + max(0, max(b))
    print(result)
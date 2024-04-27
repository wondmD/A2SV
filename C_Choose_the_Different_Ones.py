from itertools import combinations

def is_possible(a, b, k):
    for subset_a in combinations(a, k // 2):
        for subset_b in combinations(b, k // 2):
            if set(subset_a) | set(subset_b) == set(range(1, k + 1)):
                return "YES"
    return "NO"
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(is_possible(a, b, k))

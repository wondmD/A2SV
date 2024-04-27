
from collections import defaultdict

n = int(input())
for _ in range(n):
    leng = int(input())
    arr = list(map(int, input().split()))

    count_d = defaultdict(int)
    freq_d = defaultdict(int)

    for item in arr:
        count_d[item] += 1
        current_count = count_d[item]
        freq_d[current_count] += current_count

    max_appearance = max(freq_d.values())

    print(leng - max_appearance)
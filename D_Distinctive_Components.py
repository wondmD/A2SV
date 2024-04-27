def count_special_elements(n, a):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    special_count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if prefix_sum[j] - prefix_sum[i] == a[i - 1]:
                special_count += 1

    return special_count

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = count_special_elements(n, a)
    print(result)

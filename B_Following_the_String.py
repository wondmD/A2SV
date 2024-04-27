def construct_string(trace):
    n = len(trace)
    s = ['a'] * n
    count = [0] * 26

    for i in range(n):
        s[i] = chr(count[trace[i]] + ord('a'))
        count[trace[i]] += 1

    return ''.join(s)
t = int(input())

for _ in range(t):
    n = int(input())
    trace = list(map(int, input().split()))
    print(construct_string(trace))

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    underlines = 0
    i = 0

    while i < n:
        if s[i] == 'w':
            underlines += 1
            i += 1
        elif i < n - 1 and s[i:i+2] == 'vv':
            underlines += 1
            i += 2
        else:
            i += 1

    print(underlines)

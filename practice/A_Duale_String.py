for _ in range(int(input())):
    s = input()
    n = len(s)
    if s[:n//2] == s[n//2:]:
        print("YES")
    else:
        print('NO')
for tc in range(int(input())):
    n = int(input())
    s = input()
    l = 0
    r = 0

    for i in range(n):
        if s[i] == 'B':
            l = i
            break
    for i in range(n-1,0,-1):
        if s[i] == 'B':
            r = i
            break
    print (1+r-l)
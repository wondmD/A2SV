for tes_case in range(int(input())):
    s = ''
    for i in range(8):
        l = list(input())
        for c in l:
            if c != '.':
                s+=c
    print(s)
    
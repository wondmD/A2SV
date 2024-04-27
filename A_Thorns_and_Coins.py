for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0 
    for i in range(1,n):
        if s[i] == '@':
            c+=1
        if s[i] == '*' and s[i-1] == '*':
            break 

    print (c)
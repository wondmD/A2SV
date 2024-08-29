for i in range(int(input())):
    n = int(input())
    c = 0
    while n > 1:
        c+=1
        if n%5 ==0:
            n = (n*4)//5
        elif n%3 ==0:
            n = (n*2)//3
        elif n%2 == 0:
            n//=2
        else:
            break
    if n== 1:
        print(c)
    else:
        print(-1)
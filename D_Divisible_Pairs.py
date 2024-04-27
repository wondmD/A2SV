for _ in range(int(input())):
    n, x,y = map(int, input().split())
    my_list = list(map(int, input().split()))
    c =0
    for i in range(n-1):
        for j in range(i+1, n):
            if (my_list[i] + my_list[j]) % x == 0 and (my_list[i] - my_list[j]) % y == 0 :
                c+=1
    print (c)
                
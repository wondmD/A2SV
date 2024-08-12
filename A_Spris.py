    a = int(input())
    b = int(input())
    c = int(input())

    ans = 0
    arr = [a,b,c]
    while True:

        st = True
        for i in range(3):
            if i == 0:
                arr[i]-=1
                if arr[i]<0:
                    st = False
                    break
            elif i == 1:
                arr[i]-=2
                if arr[i]<0:
                    st = False
                    break

            elif i == 2:
                arr[i]-=4
                if arr[i]<0:
                    st = False
                    break
            
        if not st:
            break
        else:
            ans += 7
    print(ans)
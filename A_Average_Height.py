for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    ev = []
    od = []
    for i in range(n):
        if arr[i]%2 == 0:
            ev.append(arr[i])
        else:
            od.append(arr[i])
    if len(ev) >= len(od):
        out = ev+od
        for i in out:
            print (i, end=" ")
        print("")
    else:
        out = od+ev
        for i in out:
            print (i, end=" ")
        print("")
def sol():
    n = int(input())
    lis =[]
    for i in range(n):
        lis.append(list(map(int, input().split())))
    sums =set([])
    for i in range(n):
        for j in range(n):
            num = lis[i][j]
            found = 0
            # print(num)
            if num >1:
                row = lis[i]
                # print(num)
                # print(row)
                col = [lis[k][j] for k in range(n) ]
                # print(col)
                for idx in row:
                    for idx2 in col:
                        if idx+ idx2 == num:
                            found = 1
                            break
            if not found and num!=1:
                return "No"
    return "Yes"
print(sol())
        


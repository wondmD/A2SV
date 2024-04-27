for tc in range(int(input())):
    n = int(input())
    com = input()
    sum_ = 0
    result = []
    for i in range(n):
        if com[i] == "L":
            sum_ += i
            result.append(max(i,n-i-1)-i)
        else:
            sum_ += n - 1 - i
            result.append(max(i,n-1-i)-(n-i-1))
    result.sort(reverse=True)
    for i in range(len(result)):
        sum_+=result[i]
        result[i] = sum_ 
    print(*result)
    

for tc in range(int(input())):
    n = int(input())
    s = input()
    left = s[:n//2]
    if n%2==1:
        right = s[(n//2)+1:]
    else:
        right = s[n//2:]
    rr = right[::-1]
    p = 0
    c = 0
    while p < n//2:
        if left[p]==rr[p]:
            p+=1
        else:
            c += 1
            while (p < n//2):
                if left[p] == rr[p]:
                    break
                p+=1
    if c > 1:
        print('No')
    else :
        print('Yes')

    

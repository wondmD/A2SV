for tc in range(int(input())):
    n, k = map(int, input().split())
    blocks = input()
    left = 0 
    right = k-1
    cb = 0
    max_ = cb
    for i in range(k):
        if blocks[i] == 'B':
            cb +=1
    
    max_ = cb
    while (right < len(blocks)-1 and cb < k):
        if blocks[left] == 'B':
            cb -= 1
        right +=1
        left +=1
        
        if blocks[right] == 'B':
            cb+=1
        
        max_ = max(cb , max_)
    print (k - max_)
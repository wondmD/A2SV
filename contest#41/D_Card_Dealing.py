def sol():
    num = int(input())
    last = 1
    ger =0
    bob= 0
    while num > 0:
        if num >= last:
            ger += last
            num-= last
            last+=4
        else:
            ger += num
            num =0
        if num >= last:
            bob += last
            num-= last
            last+=4
        else:
            bob += num
            num =0
        
    return [ger, bob]
for i in range(int(input())):
    print(*sol())
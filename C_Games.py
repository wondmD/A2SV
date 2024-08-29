def sol():
    n = int(input())
    lis = list(map(int, input().split()))
    evens = []
    odds = []
    odd_sum = 0
    even_sum = 0
    for i in lis:
        if i % 2 == 0:
            evens.append(i)
            even_sum += i
        else:
            odds.append(i)
            odd_sum += i
    evens.sort()
    odds.sort()
    alice = 0
    bob =0
    if odd_sum ==0 and even_sum >0:
        print('Alice')
        return
    elif even_sum == 0 and odd_sum >0:
        print('Bob')
        return
    elif even_sum == odd_sum ==0:
        print('Tie')
        return
    while evens and odds:
        if even_sum > odd_sum:
            val = evens.pop()
            alice += val
            even_sum -= val
        else:
            val = odds.pop()
            odd_sum -= val
        if odd_sum > even_sum:
            val = odds.pop()
            bob += val
            odd_sum -= val
        else:
            val = evens.pop()
            even_sum -= val

    if alice+even_sum > bob+odd_sum:
        print("Alice")
    elif bob+odd_sum > alice+even_sum:
        print("Bob")
    else:
        print("Tie")

for _ in range(int(input())):
    sol()

    


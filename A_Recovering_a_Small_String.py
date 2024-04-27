for _  in range(int(input())):
    n = int(input())
    a = 1
    b = 1
    c = 1
    n -= 3
    while n >0 and c < 26:
        c+=1
        n-=1
    while n > 0 and b < 26:
        b+=1
        n-=1
    while n > 0 and a < 26:
        a+=1
        n-=1
    print(chr(a + ord('a')-1) + chr(b+ ord('a')-1) +chr(c+ ord('a')-1))

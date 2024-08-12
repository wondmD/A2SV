for _ in range(int(input())):
    n = int(input())
    line = input()
    value = n - line.count(')(')

    print(value)
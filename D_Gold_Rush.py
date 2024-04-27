for _ in range(int(input())):
    n, m = map(int, input().split())

    def magic(n):
        if n == m:
            return True
        elif n %3 != 0:
            return False
        
        x = magic(n - (n//3))
        y = magic(n//3)
        return x or y
    print('YES' if magic(n) else 'NO')

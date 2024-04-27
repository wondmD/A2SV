def sol():
    n = int(input())
    if n%2:
        return (n-1)//2
    return n//2
for _ in range(int(input())):
    print(sol())
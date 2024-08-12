# while True:
a, b, c, d = map(int, input().split())
x = max(int(3 * a / 10), a - int(a / 250) * c)
y = max(int(3 * b / 10), b - int(b / 250) * d)
if x == y:
    print("Tie")
elif x > y:
    print("Misha")
else:
    print("Vasya")
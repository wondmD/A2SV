def can_form_other_rectangle(a, b):
    l = [a,b]
    if a%2 == 1 and b%2 == 1:
        return ('No')
    if b % 2 == 0:
        #form new rectangle by deviding by two and then rotating and merging
        sub = b // 2
        if sub != b and sub!=a:
            return ('Yes')
    if a % 2 == 0:
        #form new rectangle by deviding by two and then rotating and merging
        sub = a // 2
        if sub != b and sub!=a:
            return ('Yes')
    return ('No')
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(can_form_other_rectangle(a, b))
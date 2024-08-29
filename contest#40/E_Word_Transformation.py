from collections import Counter

def sol():
    a, b = input().split()

    a = "".join(reversed(a))
    ans = []
    x = list(reversed(b))
    set_ = Counter(x)
    idx = 0
    for char in x:
        # print(char)
        for i in range(idx, len(a)):
            idx = idx+1
            if a[i] == char:
                ans.append(char)
                if set_[a[i]] > 1:
                    set_[a[i]]-=1
                else:
                    del set_[a[i]]

                break
            elif a[i] in set_:
                return "NO"
    if "".join(reversed(ans)) == b:
     
        return "YES"
    return "NO"

for i in range(int(input())):
    print(sol())
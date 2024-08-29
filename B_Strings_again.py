def sol():
    n,m,k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())
    if "".join(a) < "".join(b):
        target = a
        nontarget = b
    else:
        target = b
        nontarget = a
    ans = []
    target.reverse()
    nontarget.reverse()
    ct = 0
    cn =0
    while target and nontarget:
        if ct == k:
            ans.append(nontarget.pop())
            ct = 0
            cn +=1
        elif cn == k:
            ans.append(target.pop())
            cn = 0
            ct += 1
        else:
            if target[-1] <= nontarget[-1]:
                ans.append(target.pop())
                ct +=1
                cn = 0
            else:
                ans.append(nontarget.pop())
                cn +=1
                ct =0
    return("".join(ans))

for _ in range(int(input())):
    print(sol())



        

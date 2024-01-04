n =4
c = 1
tot = 0
mon = 1
print(c)
for i in range(1,n+1):
    if (i %7 == 1):
        tot+= mon
        mon +=1
        c = mon 
    else :
        tot += c
        c+=1
    print (c)
print (tot)
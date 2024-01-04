mov = input()
my_l = 'ah18'
if (mov[0] in my_l and mov[1] not in my_l) or (mov[0] not in my_l and mov[1] in my_l):
    print (5)
elif (mov[0] in my_l and mov[1] in my_l):
    print (3)
else:
    print (8)
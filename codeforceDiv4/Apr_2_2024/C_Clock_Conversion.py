from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right

def sol():
    s = stdin.readline()
    hr,mi =  map(int, s.split(':'))
    if hr == 0:
        return ("12:" +'0'*(2-len(str(mi)))+ str(mi) + " AM")
    elif hr < 12:
        return ('0'*(2-len(str(hr))) + str(hr)+":"+ '0'*(2-len(str(mi)))+str(mi) + " AM")
    elif hr == 12:
        return ('0'*(2-len(str(hr))) + str(hr)+":"+ '0'*(2-len(str(mi)))+str(mi) + " PM")
        
    else:
        hr -= 12
        return ('0'*(2-len(str(hr))) + str(hr)+":"+ '0'*(2-len(str(mi)))+str(mi) + " PM")


for _ in range(int(input())):
    print(sol())
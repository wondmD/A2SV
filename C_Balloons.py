from sys import stdin
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


def main():
    N = int(input())
    arr = list(map(int, stdin.readline().split()))
    
    if N == 1:
        print(-1)
    elif N == 2:
        if arr[1] == arr[2]:
            print(-1)
        else:
            print(1)
            print(1)
    else:
        if arr[1] != sum(arr[2:]):
            print(1)
            print(1)
        else:
            print(1)
            print(2)

if __name__ == "__main__":
    main()
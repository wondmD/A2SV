class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        d1 = defaultdict(int)
        stack1 = []
        n = len(arr)

        for i, x in enumerate(arr):
            d1[(x,i)] = n-i
            if not stack1 or stack1[-1][0] < x:
                stack1.append([x,i])
            else:
                while stack1 and x <= stack1[-1][0]:
                    poped = stack1.pop()
                    d1[(poped[0],poped[1])] = i - poped[1]
                stack1.append([x,i])
        d2 = defaultdict(int)
        stack2 = []
        arr.reverse()

        for i, x in enumerate(arr):
            d2[(x,n-i-1)] = n-i-1
            if not stack2 or stack2[-1][0] < x:
                stack2.append([x,n-i-1])
            else:
                while stack2 and x < stack2[-1][0]:
                    poped = stack2.pop()
                    d2[(poped[0],poped[1])] = abs((n-i-1) - poped[1])-1
                stack2.append([x,n-i-1])
        mod = 10**9 + 7
        arr.reverse()
        ans = 0
        for i,x  in enumerate(arr):
            ans+=(d1[(x,i)] * d2[(x,i)] + d1[(x,i)]) * x
        return  ans%mod

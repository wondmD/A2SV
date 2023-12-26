class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        l = [1] * n
        idx = n-1
        k -= n
        while k > 0 and idx >=0:
            while l[idx] < 26 and k>0:
                l[idx] += 1
                k -= 1
            idx -= 1
        s = ""
        for i in l:
            s+= chr(ord('a')-1 + i)
        return (s)

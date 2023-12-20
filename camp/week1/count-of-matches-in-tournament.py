class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n > 1:
            if  n%2 == 1:
                m+= ((n//2)+1)
                n  = n//2
            else :
                m+= n//2
                n = n//2
        return (m)
        
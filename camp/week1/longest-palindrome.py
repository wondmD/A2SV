class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = Counter(s)

        s = 0
        f = 0
        for i in x:
            if x[i] % 2==0:
                s+=x[i]
            else:
                s+= x[i]-1
                f =1
        return s+f
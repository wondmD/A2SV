class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        def reverse (i,j):
            if i > j:
                return 
            s[i], s[j] = s[j], s[i]
            reverse(i+1,j-1)
            i+=1
            j-=1
        reverse(i,j)        
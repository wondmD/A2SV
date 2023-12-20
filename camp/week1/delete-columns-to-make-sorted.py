class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        d =0
        n = len(strs)
        while c < len(strs[0]):
            s = []
            for i in range(n):
                s.append(strs[i][c])
            if sorted(s) != s:
                d+=1
            c+=1
        return (d)
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i in range(len(s)):
            d[indices[i]] = s[i]
        ss =""
        for i in range(len(s)):
            ss+=d[i]
        return (ss)
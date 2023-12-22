class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)

        d = Counter(arr)
        for i in d:
            if d[i]/n>0.25:
                return (i)
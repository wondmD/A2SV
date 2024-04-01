class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
        numss = sorted(nums)
        for i in range (len(nums)):
            if numss[i] == target:
                l.append(i)
        return (sorted(l))
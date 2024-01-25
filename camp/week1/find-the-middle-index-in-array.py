class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ps = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            ps.append(ps[i-1]+nums[i])
        for i in range(n):
            if ps[i]-nums[i] == ps[n-1]- ps[i]:
                return (i)
        return (-1)
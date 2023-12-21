class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_org = nums[:]
        nums.sort()
        if nums_org == nums:
            return (True)
        n = len(nums)
        for i in range(n-1):
            if nums_org[-2]>nums_org[-1]:
                nums_org[-1]=nums_org[-2]
                break
            if i < n-2 and nums_org[i] > nums_org[i+1] and nums_org[i] < nums_org[i+2]:
                nums_org[i+1] = nums_org[i+2]
                break
            if nums_org[i] > nums_org[i+1]:
                nums_org[i] = nums_org[i+1]
                break
        if nums_org == sorted(nums_org):
            return (True)
        return (False)



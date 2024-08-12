class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        tot = sum(nums)
        nums.sort(reverse =True)
        print (nums)
        for i in range(len(nums)-2):
            tot -= nums[i]
            if nums[i] < tot:
                return tot + nums[i]
        return -1
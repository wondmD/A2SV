class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = n - (zeros+ones)
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros, zeros+ones):
            nums[i] = 1
        for i in range(zeros+ones, n):
            nums[i] = 2
        
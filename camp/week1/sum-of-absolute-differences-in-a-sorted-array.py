class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        result[0] = sum(nums) - n * nums[0]
        for i in range(1, n):
            result[i] = result[i-1] + (nums[i] - nums[i-1]) * i - (nums[i] - nums[i-1]) * (n - i)

        return result
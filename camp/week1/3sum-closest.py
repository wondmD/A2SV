class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return target

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
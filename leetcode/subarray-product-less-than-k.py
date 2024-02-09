class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        product = 1
        subarrays = 0
        while j < len(nums):
            if j < len(nums) and product * nums[j] < k:
                product *= nums[j]
                subarrays +=j-i
                j += 1
            elif i < j:
                product //= nums[i]
                i += 1
                if product<k:
                    subarrays += 1
            else:
                i += 1
                j += 1
        subarrays += j - i
        

        return subarrays
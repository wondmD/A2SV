class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [0] * n
        prefixProduct[0] = 1

        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]

        suffixProduct = 1
        for i in range(n-1, -1, -1):
            prefixProduct[i] *= suffixProduct
            suffixProduct *= nums[i]

        return prefixProduct

        


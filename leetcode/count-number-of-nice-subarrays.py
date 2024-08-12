class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        NumberOfNice = 0
        number_of_odds = 0
        sub_subarrays = 0
        for right in range(len(nums)):
            if nums[right]%2 != 0:
                number_of_odds += 1
                sub_subarrays = 0
            if number_of_odds == k:
                while left < len(nums) and nums[left] % 2 ==0:
                    sub_subarrays+=1
                    left += 1
                sub_subarrays += 1
                number_of_odds -= 1
                left += 1
            NumberOfNice += sub_subarrays
        return NumberOfNice
                

            

            
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        max_ = 0 
        ptr1 = 0 
        ptr2 = 0
        zero_count = 0
        while ptr2 < len(nums):
            if nums[ptr2] == 1:
                ptr2 += 1
                max_=  max(max_, ptr2-ptr1)
            elif nums[ptr2] == 0 and zero_count < k:
                ptr2 += 1
                max_=  max(max_, ptr2-ptr1)
                zero_count+=1
            elif nums[ptr1] == 0:
                ptr1+=1
                zero_count -= 1
            else:
                ptr1+=1
        return (max_-1)
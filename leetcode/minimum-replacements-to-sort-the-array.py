class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        min_ = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > min_:
                slots = math.ceil(nums[i]/ min_)
                res += slots-1
                min_ = nums[i]//slots
            else :
                min_ = nums[i]
        return res
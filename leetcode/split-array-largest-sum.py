class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        low = max(nums)
        high = sum(nums)

        n = len(nums)
        best = low
        while low <= high:
            mid =  low + (high - low)//2
            part = 1
            sm = 0
            for i in nums:
                if sm + i > mid:
                    part +=1
                    sm = 0
                sm += i
            if part <= k:
                high = mid - 1
            else:
                low = mid + 1
      
        return low
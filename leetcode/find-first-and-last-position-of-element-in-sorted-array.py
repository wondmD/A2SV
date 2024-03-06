class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        end =-1
        start = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                if mid == n-1 or nums[mid+1] > target:
                    end = mid
                    break
                elif nums[mid+1] == target:
                    left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        left = 0
        right = n-1
        while left <= right:
            mid =(left + right)//2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] < target:
                    start = mid
                    break
                elif nums[mid-1] == target:
                    right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return [start, end]
        
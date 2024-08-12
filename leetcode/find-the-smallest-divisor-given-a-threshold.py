class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def valid_div(x):
            ans =0 
            for i in nums:
                ans += math.ceil(i/x)
            return ans <= threshold
        left, right = 1, max(nums)
        _min = float('inf')
        while left <= right:
            mid = (left + right) //2
            if valid_div(mid):
                _min = min(_min, mid)
                right = mid-1
            else:
                left = mid+1
        return _min


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        q.append([-1, 0])

        _sum = 0
        ans = float('inf')

        for i in range(n):
            _sum += nums[i]
            while q and _sum - q[0][1] >= k:
                ans = min(ans, i - q.popleft()[0])

            while q and q[-1][1] >= _sum:
                q.pop()
            q.append([i, _sum])

        if ans  == float("inf"):
            return -1
        return ans
        
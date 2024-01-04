class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_counts = {}
        for num in nums:
            complement = k - num
            if complement in num_counts and num_counts[complement] > 0:
                count += 1
                num_counts[complement] -= 1
            else:
                num_counts[num] = num_counts.get(num, 0) + 1
        return count

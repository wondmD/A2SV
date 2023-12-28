class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 not in numSet:
                currLen = 1
                while num + 1 in numSet:
                    num += 1
                    currLen += 1
                maxLen = max(maxLen, currLen)

        return maxLen
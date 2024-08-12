class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lis = nums[:] + nums[:]
        stack = []
        res = defaultdict(lambda: -1)
        for i,num in enumerate(lis):
            while stack and stack[-1][1]< num:
                res[(stack[-1][0],stack[-1][1])] = num
                stack.pop()
            stack.append((i,num))
        return [ res[(i, nums[i])] for i in range(len(nums))]
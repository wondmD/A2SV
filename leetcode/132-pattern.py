class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        _max = float("-inf")

        for i in range(len(nums)-1 , -1 , -1):
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] < stack[-1] and nums[i] < _max:
                    return True
                else:
                    while stack and stack[-1] < nums[i]:
                        x = stack.pop()
                        _max = max(x, _max)
                    stack.append(nums[i])
        return False

 
                    
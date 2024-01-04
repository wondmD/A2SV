class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i  in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        print (nums)
        write = 0
        read = 0
        while read < n:
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write = write + 1
            read = read + 1
        return (nums)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def majic(start, path):
            if len(path) == len(nums):
                return
            for i in range(start, len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    majic(i,path)
                    res.append(path[:])
                    path.pop()
        res = [[]]
        majic(0, [])
        return res
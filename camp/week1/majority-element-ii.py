class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_d = Counter(nums)
        n = len(nums)
        output = []
        for i in range(n):
            if my_d[nums[i]] > (n/3) and nums[i] not in output:
                output.append(nums[i])
        return (output)
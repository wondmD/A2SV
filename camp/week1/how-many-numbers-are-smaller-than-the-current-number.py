class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101  
        for num in nums:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1])

        return result
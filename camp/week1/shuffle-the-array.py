class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s1 = nums[:n]
        s2 = nums[n:]
        y = 0
        for i in range(n):
            nums[y] = s1[i]
            nums[y+1] = s2[i]
            y+=2
        return (nums) 
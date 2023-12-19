class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        c= 0
        for i in nums:
            if i == 1:
                c+=1
                maxx = max(maxx,c)
            else:
                c = 0
        return (maxx)
        
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = 0
        elemnt = 1
        out = []
        while elemnt < len(nums):
            for i in range(nums[freq]):
                out.append(nums[elemnt])
            freq+=2
            elemnt+=2
        return (out)
        
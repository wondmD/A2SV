class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 =set(nums2)
        inter = list(s1 & s2)
        inter.sort()
        if len(inter)>0:
            return(inter[0])

        return (-1)
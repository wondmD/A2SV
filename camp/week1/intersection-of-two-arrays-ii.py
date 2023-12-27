class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intr = []
        n = len(nums1)
        n2 = len(nums2)
        if n <= n2:
            for i in nums1:
                if i in nums2:
                    nums2[nums2.index(i)] = -1
                    intr.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    nums1[nums1.index(i)] = -1
                    intr.append(i)
        return (intr)
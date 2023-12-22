class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [] 
        neg = []
        for i in nums:
            if i > 0 :
                pos.append(i)
            else :
                neg.append(i)
        out = []
        for i in range(len(pos)):
            out.append(pos[i])
            out.append(neg[i])
        return (out)
        
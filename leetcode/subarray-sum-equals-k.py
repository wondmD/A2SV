class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        dictn={}
        for i in accumulate(nums):
            if i-k in dictn:
                count+=dictn[i-k]
            if i==k:
                count+=1
            if i in dictn:
                dictn[i]+=1
            else:
                dictn[i]=1
        return count
        
            
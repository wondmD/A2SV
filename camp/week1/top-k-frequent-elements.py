class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d =Counter(nums)
        ans = []
        vals = []
        for i in d:
            vals.append((d[i],i))
        vals.sort(reverse = True)
        
        for i in range(k):
            ans.append(vals[i][1])
        # print(vals)
        return ans
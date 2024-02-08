class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = 0
        res = 0
        dic = {0:1}
        for num in nums:
            tot += num
            diff  = tot - k
            if diff in dic:
                res += dic[diff]
            dic[tot] = 1 + dic.get(tot, 0)
        return (res)


            
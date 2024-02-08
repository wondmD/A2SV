class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        tot = 0
        res = 0
        dic = {0:1}
        for num in nums:
            tot = (tot+num)
            mod  = tot%k
            print (mod)
            if mod in dic:
                res += dic[mod]
            dic[mod] = 1 + dic.get(mod, 0)
        print(dic)
        return (res)
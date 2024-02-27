class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans   = []
        leng = len(nums)
        def magic(ind,path,candidates):
            if len(path)==leng:
                ans.append(path[:])
                return 
            for i in range(0,len(candidates)):
                path.append(candidates[i])
                magic(i+1,path,candidates[:i]+candidates[i+1:])
                path.pop()
        magic(0,[],nums)
        return ans
        


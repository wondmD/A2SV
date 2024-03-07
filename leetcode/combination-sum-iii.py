class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        s = 0
        def combSum(idx, path, target):
            nonlocal s
            if s == target and len(path) == k:
                ans.append(path[:])
            if len(path) == k:
                path = []
                return 
            if s > n:
                path = []
                return
            for i in range(idx, 10):
                path.append(i)
                s += i
                combSum(i+1,path,target)
                s -= path.pop()
        combSum(1,[], n)
        return ans
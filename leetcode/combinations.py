class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def majic(idx, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(idx,n+1):
                path.append(i)
                majic(i+1, path)
                path.pop()
        res = []
        majic(1,[])
        return res
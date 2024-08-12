class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        cout = Counter(candidates)
        can = list(set(candidates))
        def magic(ls, ind, summ):
            if summ == target:
                res.add(tuple(sorted(ls[:])))
                return
            if summ > target or len(ls) >= len(candidates):
                return
            for i in range(ind, len(can)):
                if cout[can[i]] != 0:
                    ls.append(can[i])
                    cout[can[i]] -= 1
                    summ += can[i]
                    magic(ls, ind, summ)
                    de = ls.pop()
                    summ -= de
                    cout[de] += 1
        magic([],0,0)
        return res
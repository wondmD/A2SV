class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        nums = sorted(list(set(fronts).union(set(backs))))
        d = defaultdict(set)
        for i in range(len(fronts)):
            d[fronts[i]].add(backs[i])
        for front in nums:
            if front not in d[front]:
                return front
        return 0
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_than = defaultdict(list)
        for x, y in richer:
            richer_than[y].append(x)
        @cache
        def dfs(root):
            _min = root
            if root not in richer_than:
                return root
            
            for node in richer_than[root]:
                candidate = dfs(node)
                if quiet[_min] > quiet[candidate]:
                    _min = candidate
            return _min
        n = len(quiet)
        return list(map(dfs, range(n)))

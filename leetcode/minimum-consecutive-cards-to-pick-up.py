class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        min_ = n+1
        idx_map = {}
        for i in range(n):
            if cards[i] in idx_map:
                min_ = min(min_, i+1 - idx_map[cards[i]])
                idx_map[cards[i]] = i
            else:
                idx_map[cards[i]] = i
        if min_ > n:
            return (-1)
        else:
            return (min_)
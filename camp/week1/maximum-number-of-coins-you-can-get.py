class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        my_coin = 0
        n = len(piles)
        i = 1
        while i < 2 * (n // 3):
            my_coin += piles[i]
            i += 2
        return my_coin
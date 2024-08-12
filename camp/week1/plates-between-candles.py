class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_pos = []
        for i, ch in enumerate(s):
            if ch == '|':
                candle_pos.append(i)
        ans = []
        for x, y in queries:
            start  = bisect_left(candle_pos, x)
            end  = bisect_right(candle_pos, y)
            if start >= end:
                ans.append(0)
                continue
            d = end - start -1
            res = candle_pos[end-1] - candle_pos[start] - d
            ans.append(res)
        return ans
        
            






class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c= max(candies)
        out = []
        for i in candies:
            if i + extraCandies >= max_c:
                out.append(True)
            else :
                out.append(False)        
        return (out)
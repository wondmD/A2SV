class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
    
        for start, end in ranges:
            for x in range(start, end + 1):
                covered.add(x)
        
        for num in range(left, right + 1):
            if num not in covered:
                return False
        
        return True
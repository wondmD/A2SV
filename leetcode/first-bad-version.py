# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while right >= left:
            mid = (left+right)//2
            if isBadVersion(mid):
                if mid == 1:
                    return mid
                if not isBadVersion(mid-1):
                    return mid
                else:
                    right = mid-1
            else:
                if mid == n:
                    return mid
                if isBadVersion(mid+1):
                    return mid+1
                else:
                    left = mid+1
        return 0
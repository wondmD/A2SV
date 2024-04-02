class Solution:
    def canWinNim(self, n: int) -> bool:
        # while n > 6:
        #     n -= 6
        # if n == 4:
        #     return False
        # return True

        if n%4:
            return True
        return False

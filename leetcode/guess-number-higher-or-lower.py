# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n
        self.final = False
        self.get_pick(1, n)
        return self.final
  

    def get_pick(self,s, n):
        if self.final:
            return
        mid = (s+n) // 2
        res = guess(mid)
        #print(res, mid)
        if res == 0:
            self.final = mid
            return
        elif res == -1:
            self.get_pick(s, mid)
        else:
            self.get_pick(mid, n)

        
        
        
        



        
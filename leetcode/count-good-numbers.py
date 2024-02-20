class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        def powr(num, p,mod):
            if p == 0:
                return 1
            
            result = 1
            while p > 0:
                if p % 2 == 1:
                    result *= num
                num *= num
                num %= mod
                p //= 2
            return result
        if n % 2 == 0:
            return (powr(5,n//2, mod) * powr(4,n//2,mod)) % mod
        else:
            return (powr(5,(n//2)+1,mod) * powr(4,n//2,mod)) % mod 
        
        
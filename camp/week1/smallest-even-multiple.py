class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        p = n
        if p%2 == 1:
            p+=1
        while True:
            if p%n == 0 and p%2 == 0:
                return (p)
            p+=2
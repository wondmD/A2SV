class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        my_intiger = n
        while True:
            if my_intiger % n == 0 and my_intiger % 2 == 0:
                return (my_intiger)
            my_intiger += 1
        
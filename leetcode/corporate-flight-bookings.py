class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        opprate = [0] * (n+1)
        for first, last, seat in bookings:
            opprate[first-1] += seat
            opprate[last] -= seat
        prefix = [0]*n
        prefix[0] = opprate[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + opprate[i]
        return prefix 


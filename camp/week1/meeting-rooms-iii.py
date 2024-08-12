class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        taken=[]

        available=[i for i in range(n)]

        count=[0]*n
        
        meetings.sort()

        for start,end in meetings:
            while taken and taken[0][0]<=start:
                _end,room=heapq.heappop(taken)
                heapq.heappush(available,room)

            if available:
                room=heapq.heappop(available)
                heapq.heappush(taken,(end,room))
            else:
                time,room=heapq.heappop(taken)
                heapq.heappush(taken,(time+end-start,room))
            count[room]+=1
        return count.index(max(count))      

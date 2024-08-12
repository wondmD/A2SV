class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        time = 0
        tasks.sort()
        processorTime.sort()
        idx = 0
        for j in range(len(tasks)-1,-1,-4):
            i = processorTime[idx]
            time=max(time,i+tasks[j],i+tasks[j-1],i+tasks[j-2],i+tasks[j-3])
            idx+=1
        return (time)             

        
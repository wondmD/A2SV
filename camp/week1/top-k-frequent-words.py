class Solution:
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        freq = Counter(nums)
        heap = []
        for i in freq:
            heapq.heappush(heap,(-freq[i], i))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
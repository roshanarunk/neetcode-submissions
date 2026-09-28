class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify_max(heap)

        for x in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, x)
            else:
                heapq.heappush(heap, x)
        return heapq.heappop(heap)
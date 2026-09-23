class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            print(y, x)
            if y != x:
                heapq.heappush_max(stones, y - x)
        return heapq.heappop(stones) if len(stones) == 1 else 0
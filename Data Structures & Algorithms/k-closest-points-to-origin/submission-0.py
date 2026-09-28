class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eDist(x,y):
            return math.sqrt(x*x + y*y)
        
        heap = []
        heapq.heapify_max(heap)

        for p in points:
            if len(heap) == k:
                dist = eDist(p[0],p[1])
                if dist < heap[0][0]:
                    heapq.heappushpop_max(heap, (dist, p[0],p[1]))
            else:
                heapq.heappush_max(heap, (eDist(p[0],p[1]), p[0],p[1]))
        
        res = []

        while len(heap) > 0:
            x = heapq.heappop_max(heap)
            res.append([x[1], x[2]])
        return res

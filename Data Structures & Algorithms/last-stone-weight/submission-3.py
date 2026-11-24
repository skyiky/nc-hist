import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            z = x - y
            if z > 0:
                heapq.heappush_max(stones, z)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

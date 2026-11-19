import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k1, k2 = 1, max(piles)
        while k1 < k2: # binary search
            k = (k1 + k2) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            if t > h:
                k1 = k + 1
            else: # t <= h
                k2 = k
        return k1

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rateLow, rateHigh = 1, max(piles)
        while rateLow < rateHigh:
            rateMid = (rateLow + rateHigh) // 2
            timeTotal = 0
            for bananas in piles:
                timeElapsed = math.ceil(bananas / rateMid)
                timeTotal += timeElapsed
            if timeTotal > h: # too slow
                rateLow = rateMid + 1
            if timeTotal <= h: # valid
                rateHigh = rateMid
            
        return rateLow

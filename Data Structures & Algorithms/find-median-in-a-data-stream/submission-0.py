import heapq
class MedianFinder:

    def __init__(self):
        self.small = []  # Max-heap, stored as negatives
        self.large = []  # Min-heap
    
    # An invariant is a rule that must hold before and after each operation. It can temporarily
    #   break inside the operation.
    # Invariant: All small values ≤ all large values
    # Invariant: Sizes differ by at most 1
    # After inserting one value:
    # - Only that new value can violate the ordering.
    # - If it does, it must be small’s maximum.
    # - Therefore, moving one root fixes the ordering. No search is needed.
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # This is invariant maintenance, using an “update, then repair” pattern.
        # Fix ordering: small's maximum must not exceed large's minimum.
        if self.large and -self.small[0] > self.large[0]:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Fix sizes: neither heap may have more than one extra value.
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2
        
        
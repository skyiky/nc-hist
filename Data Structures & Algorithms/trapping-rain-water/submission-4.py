class Solution:
    # two pointer converging approach, imagine a "fog of war" in the middle, so l and r cannot see each other, but they are able to report lmax and rmax to each other. This is enough information to determine how much water l or r can hold.
    def trap(self, height: List[int]) -> int:
        water = 0
        lmax = 0
        rmax = 0

        l = 0
        r = len(height) - 1
        while l <= r: # invariant: pointers are unprocessed work, so l == r means there is 1 unprocessed column remaining
            if lmax <= rmax:
                lmax = max(lmax, height[l])
                water += (lmax - height[l])
                l += 1
            else:
                rmax = max(rmax, height[r])
                water += (rmax - height[r])
                r -= 1

        return water


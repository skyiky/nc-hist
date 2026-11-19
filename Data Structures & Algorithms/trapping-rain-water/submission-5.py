class Solution:
    def trap(self, height: List[int]) -> int:
        tallest_l, tallest_r = 0, 0
        l, r = 0, len(height)-1
        total = 0

        while l <= r:
            if tallest_l <= tallest_r:
                tallest_l = max(tallest_l, height[l])
                total += tallest_l - height[l]
                l += 1
            else:
                tallest_r = max(tallest_r, height[r])
                total += tallest_r - height[r]
                r -= 1


        return total
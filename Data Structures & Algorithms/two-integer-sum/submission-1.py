class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            c = target - n
            if c not in hmap:
                hmap[n] = i
            else:
                return [hmap[c], i]

            
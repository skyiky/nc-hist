class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def backtrack(start):
            result.append(path[:])
            for i in range(start, len(nums)):
                # In this call’s loop, have I already tried this value as the next choice?
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                # For walkthroughs, do not mentally expand every recursive call at once. Write its job instead:
                backtrack(i + 1) # Explore all extensions of the current path using later indices.
                path.pop()

        backtrack(0)
        return result
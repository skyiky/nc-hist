class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(start: int) -> None:
            for i in range(start, len(nums)):
                path.append(nums[i])
                result.append(path[:])
                backtrack(i + 1)
                path.pop()

        result.append(path)
        backtrack(0)
        return result
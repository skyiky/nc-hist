class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at each index i, make two choices:
        # dfs(i, path)
        # --> Include nums[i] -> dfs(i + 1)
        # --> Skip nums[i] -> dfs(i + 1)
        # i == len(nums) -> save a copy of path
        result = []
        path = []

        # "Decisions before i are fixed. Explore every choice from i onward. 
        #  Return with path exactly as I found it." <-- backtracking key concept
        def dfs(i):
            if i == len(nums):
                result.append(path[:])
                return
            
            # Include i and go next
            path.append(nums[i])
            dfs(i + 1)

            # Undo i and go next
            path.pop()
            dfs(i + 1)

        dfs(0)
        return result
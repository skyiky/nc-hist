class Solution:
    def rob(self, nums: List[int]) -> int:

        # dfs(i) --> returns max profit from house i to the end
        memo = {}


        def dfs(i: int) -> int:
            # base case = out of bounds
            if i >= len(nums): 
                return 0
            
            if i in memo:
                return memo[i]
            
            rob_curr = nums[i] + dfs(i+2)
            skip_curr = dfs(i+1)

            memo[i] = max(rob_curr, skip_curr)

            return memo[i]


        return dfs(0)
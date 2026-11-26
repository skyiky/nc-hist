class Solution:
    # Top-Down, right-to-left
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # cache results for (i, j)

        # Length of lis ENDING at index i
        def dfs(i :int) -> int:
            if i in memo: 
                return memo[i]

            best = 1 # nums[i] by itself is always a subsequence of length 1
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(best, 1 + dfs(j))
            memo[i] = best
            return best

        return max(dfs(i) for i in range(len(nums)))
        
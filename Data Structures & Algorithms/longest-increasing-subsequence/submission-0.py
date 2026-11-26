class Solution:
    # Top-Down, left-to-right
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} # cache results for (i, j)

        # i = current index, j = index of last chosen element (-1 if none)
        def dfs(i, j):
            if i == len(nums): # out of bounds -> return 0
                return 0
            
            if (i, j) in memo: # return cached result if already computed
                return memo[(i, j)]
            
            # exclude nums[i] (add 0, j stays unchanged)
            exclude = dfs(i+1, j)

            include = 0 # include nums[i] (add 1, and i becomes the new previously chosen index j)
            if j == -1 or nums[i] > nums[j]:
                include = 1 + dfs(i+1, i)
            
            memo[(i, j)] = max(exclude, include)
            return memo[(i, j)]

        return dfs(0, -1)
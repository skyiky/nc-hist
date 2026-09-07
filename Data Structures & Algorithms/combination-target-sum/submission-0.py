class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        path_sum = 0

        # dfs(start) explores combinations using only indices 'start' and higher,
        #   then returns with path and path_sum unchanged
        def dfs(i):
            nonlocal path_sum

            if path_sum == target:
                result.append(path[:])
                return
            if path_sum > target:
                return

            for j in range(i, len(nums)): # starting loop at i prevent reordered duplicates
                path.append(nums[j])
                path_sum += nums[j]
                dfs(j) # allow the chosen number again
                path.pop() # restore state before next 'choice'
                path_sum -= nums[j]      

        dfs(0) # start with all candidates available
        return result
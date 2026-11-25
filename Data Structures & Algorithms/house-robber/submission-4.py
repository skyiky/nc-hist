class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. Handle small input edge cases (e.g., 1 house)
        if n == 1:
            return nums[0]

        # 2. State: dp[i] = max money achievable using houses 0..i
        maxProfitHouseA = nums[0]
        maxProfitHouseB = max(nums[0], nums[1])

        maxProfitHouseC = maxProfitHouseB
        # 3. Transition for each remaining house
        for i in range(2, n):
            maxProfitHouseC = max(nums[i] + maxProfitHouseA, maxProfitHouseB) # 0,2 vs 1
            maxProfitHouseA = maxProfitHouseB
            maxProfitHouseB = maxProfitHouseC

        # 4. Final answer
        return maxProfitHouseC

    def robTopDown(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i: int) -> int:
            # 1. Base case: when i is out of bounds
            if i >= len(nums):
                return 0

            # 2. Return cached result if already computed
            if i in memo:
                return memo[i]

            # 3. Two choices at house i:
            #    - rob house i (where can you go next?)
            #    - skip house i (where can you go next?)
            rob_curr = nums[i] + dfs(i+2)
            skip_curr = dfs(i+1)

            # 4. Cache and return the better choice
            memo[i] = max(rob_curr, skip_curr)
            return memo[i]

        return dfs(0)
class Solution:
    def robBottomUp(self, nums: List[int]) -> int:
        maxProfitHouseA = 0
        maxProfitHouseB = 0
        for num in nums:
            maxProfitHouseC = max(num + maxProfitHouseA, maxProfitHouseB) # 0,2 vs 1
            maxProfitHouseA = maxProfitHouseB
            maxProfitHouseB = maxProfitHouseC
        return maxProfitHouseB

    def rob(self, nums: List[int]) -> int:
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
        print(memo)

        return dfs(0)
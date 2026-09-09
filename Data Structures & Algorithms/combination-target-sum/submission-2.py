class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        def backtrack(i, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for j in range(i, len(nums)):
                value = nums[j]
                if value > remaining:
                    return
                path.append(value)
                backtrack(j, remaining - value)
                path.pop()


        
        backtrack(0, target)
        return result
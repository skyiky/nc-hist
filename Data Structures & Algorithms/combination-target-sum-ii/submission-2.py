class Solution:
    # Save?     When path sum == target
    # Choose?   Cannot reuse, choose next
    # Stop?     Stop when path sum > target
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                value = candidates[i]
                if value > remaining:
                    return
                    
                path.append(value)
                backtrack(i + 1, remaining - value)
                path.pop()
            

        backtrack(0, target)
        return result
        
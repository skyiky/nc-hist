class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(candidates, level):
            if not candidates:
                result.append(path.copy())
                return

            for n in candidates:
                path.append(n)
                next_candidates = candidates.copy()
                next_candidates.remove(n)
                backtrack(next_candidates, level + 1)
                path.pop()
            
        backtrack(set(nums), 0)
        return result

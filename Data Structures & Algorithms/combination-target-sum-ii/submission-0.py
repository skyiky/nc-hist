class Solution:
    # For [1a, 1b, 2], target 3:
    # Choose 1a → choose 2 → [1,2]
    # Choose 1b → choose 2 → [1,2]  ← duplicate, so skip this branch
    # The first 1 has access to all the later candidates available to the second 1, plus the second 1 itself. So we lose nothing by skipping the second 1 as an alternative at the same level.
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        # appends to result every unique combination that extends the current path using candidates at indices start onward to sum to remaining, leaving path unchanged when it returns
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                # skip duplicates, first occurence already explored the branch
                if (i > start # always process first candidate: i == start
                    and candidates[i] == candidates[i-1]):
                        continue # skip
                # If this candidate misses the target, so do all the later ones since sorted
                if candidates[i] > remaining:
                    break
                # Choose
                path.append(candidates[i])
                # Explore later indices
                backtrack(i + 1, remaining - candidates[i])
                # Undo
                path.pop()
        backtrack(0, target)
        return result
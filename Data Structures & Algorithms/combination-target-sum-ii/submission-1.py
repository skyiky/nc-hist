
class Solution:
    # For [1a, 1b, 2], target 3:
    # path = []
    #   → pick 1a
    #   → skip 1b
    #   → pick 2
    # 1a has access to all the same later candidates as 1b (and also 1b itself)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        # backtrack(start, remaining): appends to result every unique combination that
        #   extends the current path using candidates at indices start onward 
        #   to sum to remaining, leaving path unchanged when it returns
        # Each call needs three pieces of information:
        #   path        # What have I chosen?
        #   start       # Which indices can I choose next?
        #   remaining   # How much more do I need?
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            # "The loop explores alternatives; recursion extends the current choice"
            for i in range(start, len(candidates)):
                # Among sibling branches, choose each distinct value only once.
                # (i > start): dont skip first candidate, prevent skipping in case: path=[1], candidates[i]=1
                if (i > start and candidates[i] == candidates[i-1]):
                        continue
                # If this candidate overshoots the target, so do all later candidates
                if candidates[i] > remaining:
                    return

                path.append(candidates[i]) # Choose
                backtrack(i + 1, remaining - candidates[i]) # Explore
                path.pop() # Undo

        backtrack(0, target)
        return result
    # A repeated value is allowed to extend a path, but skipped when it would repeat a sibling branch.
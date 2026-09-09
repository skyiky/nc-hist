class Solution:
    # Decision	                        Subsets	                        Combination Sum
    # Save: Is this path an answer?	    Every path is a valid subset	Only when its sum equals target
    # Choose: Can I reuse this number?	No: continue from j + 1	        Yes: continue from j
    # Stop: Can this branch grow?	    Until no candidates remain	    Until the target is reached or no candidate fits
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
# Reusable Checklist
# For backtracking problems, separate:
# - Answers: How many completed answers can exist?
# - Saving: How much work to store each answer?
# - Searching: Can exploring partial or rejected choices cost more?
# "Number of answers × cost per answer" is a useful starting point, not a universal rule. Lots of rejected branches can make other problems # more expensive.
class Solution:
    # The State
    # At the start of every dfs(start) call:
    # Region	    Meaning
    # s[:start] -->	Already partitioned into the palindromes in path
    # s[start:]	--> Still needs to be partitioned
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(s) -> bool:
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # dfs(start):
        # 1. Extends path with every palindromic partition of s[start:]
        # 2. Append each completed partition to result
        def dfs(start):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)): # Try different endings for the next substring
                x = s[start:i+1]
                if isPalindrome(x):
                    path.append(x)
                    dfs(i+1) # After choosing that substring, partition what remains
                    path.pop() # 

        dfs(0)
        return result
        # For "aab", the choices form this tree:
        # []                           remaining: "aab"
        # ├── choose "a"
        # │   ["a"]                    remaining: "ab"
        # │   ├── choose "a"
        # │   │   ["a", "a"]           remaining: "b"
        # │   │   └── choose "b"
        # │   │       ["a", "a", "b"]  remaining: "" → save copy
        # │   └── reject "ab"
        # ├── choose "aa"
        # │   ["aa"]                   remaining: "b"
        # │   └── choose "b"
        # │       ["aa", "b"]          remaining: "" → save copy
        # └── reject "aab"
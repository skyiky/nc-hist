class Solution:
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

        # dfs(start) appends to result, all possible lists of palindromic substrings for string s[start:]
        def dfs(start):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                x = s[start:i+1]
                if isPalindrome(x):
                    path.append(x)
                    dfs(i+1)
                    path.pop()

        dfs(0)
        return result
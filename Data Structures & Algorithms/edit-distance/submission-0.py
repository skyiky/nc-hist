class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        # dfs(i, j) = minimum number of edits required to make w1[:i+1] equal w2[:j+1]
        def dfs(i, j) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1  # (Bonus: when both are -1, j + 1 automatically returns 0.)

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i-1, j-1) # move both pointers back

            delete_curr = 1 + dfs(i-1, j)
            insert_curr = 1 + dfs(i, j-1)
            replace_curr = 1 + dfs(i-1, j-1)
            memo[(i, j)] = min(delete_curr, insert_curr, replace_curr)
            return memo[(i, j)]

        return dfs(len(word1)-1, len(word2)-1) 
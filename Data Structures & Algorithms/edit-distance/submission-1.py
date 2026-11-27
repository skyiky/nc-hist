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

        rows = len(word1)+1
        cols = len(word2)+1
        def bottomUp() -> int:
            dp = [[0] * cols for _ in range(rows)]
            for j in range(cols):
                dp[0][j] = j
            for i in range(rows):
                dp[i][0] = i
            for i in range(1, rows):
                for j in range(1, cols):
                    if word1[i-1] == word2[j-1]:
                        continue
                    delete_curr = 1 + dp[i-1][j]
                    insert_curr = 1 + dp[i][j-1]
                    replace_curr = 1 + dp[i-1][j-1]
                    dp[i][j] = min(delete_curr, insert_curr, replace_curr)
            return dp[-1][-1]








            
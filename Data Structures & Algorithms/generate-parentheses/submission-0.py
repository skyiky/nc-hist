class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        stack = []
        def backtrack(i):
            if i == n*2:
                if not stack:
                    result.append("".join(path))
                return 

            path.append('(')
            stack.append('(')
            backtrack(i + 1)
            path.pop()
            stack.pop()

            if stack:
                path.append(')')
                stack.pop()
                backtrack(i + 1)
                path.pop()
                stack.append('(')


        backtrack(0)
        return result
        
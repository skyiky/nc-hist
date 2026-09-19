class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        result = []
        path = []
        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i: int) -> None:
            if i == len(digits):
                result.append("".join(path))
                return

            d = digits[i]
            for c in hmap[d]:
                path.append(c)
                dfs(i+1)
                path.pop()

        dfs(0)
        return result
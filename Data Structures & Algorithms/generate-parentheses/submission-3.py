class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        stack = []
        # Anchor 1: The Promise
        # INPUT
        # path  = a prefix of length i
        # stack = the unmatched '(' in that prefix    
        #
        # JOB
        # Find every valid length-2*n string extending this prefix.
        #
        # ON RETURN
        # Leave path and stack exactly as they were on entry.
        # ^ This lets the CALLER safetly try another choice
        #
        # Anchor 2: The Choices
        # There are only two possible next characters
        #
        # Anchor 3: The Undo
        # The child must restore its own changes. Then this call undoes its one choice.
        # Why can you trust the child to restore its changes?
        # - At length 2*n, the call changes neither path nor stack.
        # - One level above that, each choice is explicitly undone.
        # - The same reasoning works upward, one level at a time.
        # This is the justification for recursion, rather than mentally tracing every call.
        def backtrack(i):
            if i == n*2: # Base case / path final. (valid result always n pairs)
                if not stack: # path validity guard; open has been matched
                    result.append("".join(path))
                return 

            path.append('(')
            stack.append('(')
            backtrack(i + 1) # Choice 1, pick open
            path.pop()
            stack.pop()

            if stack: # path validity guard; to pick close, need an unmatched open
                path.append(')')
                stack.pop()
                backtrack(i + 1) # Choice 2, pick close
                path.pop()
                stack.append('(')


        backtrack(0)
        return result
        
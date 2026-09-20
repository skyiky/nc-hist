"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Pattern: Memoized Recursive Construction
#   CREATE an object
#   REGISTER it
#   CONNECT its dependencies recursively
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        memo: dict[Node, Node] = {}

        # dfs(original) returns the clone of original
        # Your work: create the current object and wire its connections
        # Recursive work: Obtain the result object for each dependency

        def dfs(original: Node) -> Node:
            if original in memo: # REUSE
                return memo[original]

            clone = Node(original.val) # CREATE
            memo[original] = clone # REGISTER
            # A dependency can point back to the object you are still building. Registering early lets that dependency reuse the same object instead of recursing forever.

            for n in original.neighbors:
                n_clone = dfs(n)
                clone.neighbors.append(n_clone) # CONNECT

            return clone

        return dfs(node)
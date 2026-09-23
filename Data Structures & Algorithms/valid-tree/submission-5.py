class Solution:
    # Pattern 1
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, parent) -> bool:
            if node in visited:
                return False

            visited.add(node) # Reaching a visited node through a different edge indicates a cycle

            for neighbor in graph[node]:
                if neighbor == parent: # Skip where I just came from
                    continue
                elif not dfs(neighbor, node): # Current node becomes parent
                    return False

            return True
            
        if not dfs(0, -1):
            return False

        return len(visited) == n

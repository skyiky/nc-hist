class Solution:
    # Adjacency list + DFS
    # Count how many times you need to start a new traversal. Each DFS visits one entire connected component
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        components = 0

        for node in range(n):
            if visited[node]:
                continue
            # An unvisited node belongs to a new component
            components += 1
            visited[node] = True
            stack = [node]

            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        return components
        
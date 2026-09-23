class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BUILD GRAPH
        graph = {  course: [] for course in range(numCourses) }
        for course, depn in prerequisites:
            graph[course].append(depn)

        visited = set()
        completed = set()
        def dfs(course, visited) -> bool:
            if course in completed:
                return True
            if course in visited:
                return False
            visited.add(course)
            for neighbor in graph[course]:
                result = dfs(neighbor, visited)
                if not result:
                    return False
            visited.remove(course)
            completed.add(course)
            return True


        for course in range(numCourses):
            result = dfs(course, visited)
            if not result:
                return False

        return True


        
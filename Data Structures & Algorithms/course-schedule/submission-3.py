class Solution:
    # Pattern: DFS Cycle Detection
    # Main Question: Does this prerequisite chain contain a cycle?
    # Tracks: Active DFS path + fully checked courses
    # Cycle detected when: DFS reaches a course already on the active path
    # Deep chains can exceed recursion limit
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {  course: [] for course in range(numCourses) }
        for course, depn in prerequisites:
            graph[course].append(depn)

        path = set()
        completed = set() # avoid redundant work, 
        def dfs(course) -> bool:
            if course in completed:
                return True
            if course in path:
                return False

            path.add(course)

            for neighbor in graph[course]:
                result = dfs(neighbor)
                if not result:
                    return False

            path.remove(course)

            completed.add(course)

            return True


        for course in range(numCourses):
            result = dfs(course)
            if not result:
                return False

        return True


        

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Step 1: Build graph and indegree array
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # Step 2: Add all courses with indegree 0
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: BFS (Topological Sort)
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses can be completed
        return count == numCourses

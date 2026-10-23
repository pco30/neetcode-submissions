class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = 0
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # BFS
        while queue:
            course = queue.popleft()
            count+=1

            for nei in adj[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)

        if count == numCourses:
            return True
        
        return False
        
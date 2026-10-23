class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adj = [[] for i in range(numCourses)]
        queue = deque()
        indegree = [0] * numCourses
        count = 0

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                ans.append(i)

        while queue:
            course = queue.popleft()
            count+=1

            for nei in adj[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
                    ans.append(nei)

        if len(ans) == numCourses:
            return ans
        
        return []
        
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        visit = set()
        edges = collections.defaultdict(list)
        minheap = [[0, k]]

        for u, v, w in times:
            edges[u].append((v, w))
        
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1 +w2, n2))

        if len(visit) == n:
            return time
        return -1
        
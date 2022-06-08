# Network Delay Time LeetCode Question
# Input k refers to the starting node
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(lists)

        for u, v, cost in times:
            g[u].append((cost, v))

        min_heap = [(0, k)]

        visited = set()
        distance = {i: float("inf") for i in range(1, n + 1)}

        distance[k] = 0

        while min_heap:
            current_distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if (len(visited)) == n:
                return current_distance

            for direct_distance, v in g[u]:
                if (
                    current_distance + direct_distance < distance[v]
                    and v not in visited
                ):
                    distance[v] = current_distance + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))

        return -1

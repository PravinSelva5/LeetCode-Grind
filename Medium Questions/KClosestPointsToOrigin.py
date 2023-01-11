class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        listDistance = [ [points[i][0] ** 2 + points[i][1] ** 2, points[i][0], points[i][1] ]
                                for i in range(len(points)) ]
        
        heapq.heapify(listDistance)
        output = []

        while k:
            distance = heapq.heappop(listDistance)
            output.append(distance[1:])
            k -= 1
        
        return output
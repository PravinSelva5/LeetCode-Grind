class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # to simulate a max heap, first need to multiply each weight by -ve
        stones = [-1 * stone for stone in stones]
        # to turn the list into a heap, must use heapify function
        heapq.heapify(stones)

        # we want to compare stone weights until there is atleast 1 stone left
        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if second < first:
                y = -1 * (first - second)
                heapq.heappush(stones, y)
        
        if len(stones) == 1:
            return -1 * heapq.heappop(stones)
        else:
            return 0

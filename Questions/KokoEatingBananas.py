class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Based on the problem, the range can be made based on the max pile value in the given array
        # for example, [3,6,7,11], the range for k would be [1,11]

        lower_bound = 1
        upper_bound = max(piles)
        minK = upper_bound

        while lower_bound <= upper_bound:
            k = (lower_bound + upper_bound) // 2
            hours = 0

            for bananas in piles:
                hours += math.ceil(bananas / k)
            
            # If the hours is less than or equal to the h provided, we can conclude the k value is sufficient.
            if hours <= h:
                minK = min(minK, k)
                upper_bound = k - 1
            else:
                lower_bound = k + 1
        
        return minK

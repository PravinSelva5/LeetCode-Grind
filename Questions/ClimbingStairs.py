class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)  # we consider stepping from 1 not 0, which is why we use n+1

        # These are the initial states that get repeated once we pass step 2.
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    

# Another Solution

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1

#         for i in range(n-1):
#             temp = one
#             one = one + two
#             two = temp 
        
#         return one



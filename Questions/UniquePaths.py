class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # unique paths to reach cell i, can be found by adding the unique paths value of the cell above it and to the left of cell i

        dp = [[0 for x in range(m)] for y in range(n)]

        # There is only one way to reach any element in the first column and row
        for i in range(m):
            dp[0][i] = 1

        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

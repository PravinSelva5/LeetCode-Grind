class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Because the question states 'return all unique combinations', this is a backtracking question.
        # Time Complexity: 2 ^(target #)

        output = []

        def dfs(i, cur, totalSum):
            # This represents the goal of the backtracking algorithm
            if totalSum == target:
                # we're going to append a copy of the cur value because it will be modified as we are recursively changing it.
                output.append(cur.copy())
                return
            # this is the constraint where we can't find a combination
            if i >= len(candidates) or totalSum > target:
                return
            
            # Recursive step
            
            cur.append(candidates[i])
            dfs(i, cur, totalSum + candidates[i] )

            # This is the decision where we aren't including the current candidate to avoid duplicates
            cur.pop()
            dfs(i + 1, cur, totalSum)
        
        dfs(0, [], 0)

        return output
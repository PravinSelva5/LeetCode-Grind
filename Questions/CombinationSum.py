class Solution:
    def solution(self, candidates, answer, current, target, index, sum):
        if sum == target:
            answer.append(current[:])
        elif sum < target:
            n = len(candidates)
            for i in range(index, n):
                current.append(candidates[i])
                self.solution(
                    candidates, answer, current, target, i, sum + candidates[i]
                )
                current.pop()
            return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        current = []
        self.solution(candidates, answer, current, target, 0, 0)

        return answer

class Solution:
    def solution(self, nums, answer, current, index):
        if index > len(nums):
            return
        answer.append(current[:])
        for i in range(index, len(nums)):
            if nums[i] not in current:
                current.append(nums[i])
                self.solution(nums, answer, current, i)
                current.pop()
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This is a backtracking/recursive problem

        answer = []
        current = []
        self.solution(nums, answer, current, 0)
        return answer

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}

        for num in nums:
            if num in m:
                # We can return True here.
                m[num] += 1
            else:
                m[num] = 1

        for i in m:
            if m[i] > 1:
                return True

        return False

class Solution:
    def backtracking(self, answer, telepad_map, digits, combination, index):
        # is the index out of bounds?
        if index > len(digits):
            return

        if len(combination) == len(digits):
            answer.append(combination[:])
            return

        currentDigit = digits[index]
        curString = telepad_map[currentDigit]

        for i in range(len(curString)):
            self.backtracking(
                answer, telepad_map, digits, combination + curString[i], index + 1
            )

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []

        # If input is an empty array
        if len(digits) == 0:
            return answer

        telepad_map = {}

        telepad_map["2"] = "abc"
        telepad_map["3"] = "def"
        telepad_map["4"] = "ghi"
        telepad_map["5"] = "jkl"
        telepad_map["6"] = "mno"
        telepad_map["7"] = "pqrs"
        telepad_map["8"] = "tuv"
        telepad_map["9"] = "wxyz"

        self.backtracking(answer, telepad_map, digits, "", 0)

        return answer

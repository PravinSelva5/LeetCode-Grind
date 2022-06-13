class Solution:
    def isEqual(self, c1, c2):
        if c1 == "(" and c2 == ")":
            return True
        if c1 == "[" and c2 == "]":
            return True
        if c1 == "{" and c2 == "}":
            return True

    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if len(stack) != 0:
                last_element = stack[-1]

                if self.isEqual(last_element, character):
                    stack.pop()
                    continue

            stack.append(character)

        return len(stack) == 0

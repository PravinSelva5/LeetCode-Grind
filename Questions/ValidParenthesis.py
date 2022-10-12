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


# Solution/ Attempt 2
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         brackets = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }
        
#         for char in s:
#             if char in brackets:
#                 # if true, that means its a closing bracket
#                 if stack and stack[-1] == brackets[char]:
#                     stack.pop()
                
#                 else:
#                     return False
#             else:
#                 stack.append(char)
        
        
#         # Only return true if stack is empty
#         return True if not stack else False
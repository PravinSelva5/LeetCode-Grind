class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non-alphanumeric characters with pythod method
        string_value = ("".join(ch for ch in s if ch.isalnum())).lower()

        start = 0
        end = len(string_value) - 1

        while start < end:
            if string_value[start] == string_value[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != mapping[char]:
                    return False

        return not stack


class Solution(object):
    def is_valid(self, s):
        """Check if a string of parentheses is valid."""
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack

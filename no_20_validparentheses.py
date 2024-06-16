class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if temp != pairs[ch]:
                        return False
        return len(stack)==0

s=Solution()
s.isValid("()")
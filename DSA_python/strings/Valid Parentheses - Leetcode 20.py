class Solution:
    def isValid(self, s: str) -> bool:
        a = {"}":"{", "]":"[", ")":"("}
        stack = []
        for i in s:
            if i not in a :
                stack.append(i)
            else:
                if stack and stack[-1] == a[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
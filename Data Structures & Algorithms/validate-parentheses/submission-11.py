class Solution:
    def isValid(self, s: str) -> bool:
        mapP = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            if c not in mapP:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapP[c]:
                return False
            stack.pop()

        return not stack

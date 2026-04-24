class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c not in pMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != pMap[c]:
                return False
            stack.pop()
        
        return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for x in s:
            if x not in Map:
                stack.append(x)
            elif not stack or Map[x] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack

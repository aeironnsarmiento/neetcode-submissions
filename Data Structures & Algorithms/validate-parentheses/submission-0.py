class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        myStack = []

        for c in s:
            if c in Map:
                if not myStack or myStack[-1] != Map[c]:
                    return False
                myStack.pop()
            else:
                myStack.append(c)

        return not myStack
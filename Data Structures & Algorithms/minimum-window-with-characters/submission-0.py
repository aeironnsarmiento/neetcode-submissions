class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        currWindow = {}
        distinct = len(countT)
        haveDistinct = 0

        bestL, bestR = -1, -1
        length = float('inf')

        l = 0
        for r in range(len(s)):
            currWindow[s[r]] = currWindow.get(s[r], 0) + 1

            if s[r] in countT and currWindow[s[r]] == countT[s[r]]:
                haveDistinct += 1

            # try to get smaller
            while haveDistinct == distinct:
                currLength = r - l + 1
                if currLength < length:
                    bestL = l
                    bestR = r
                    length = currLength
                currWindow[s[l]] -= 1

                if s[l] in countT and currWindow[s[l]] < countT[s[l]]:
                    haveDistinct -= 1
                
                l += 1

        if length == float('inf'):
            return ""

        return s[bestL:bestR + 1]
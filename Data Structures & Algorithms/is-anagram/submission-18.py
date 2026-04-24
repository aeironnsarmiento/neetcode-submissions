class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for c in range(len(s)):
            sMap[s[c]] = sMap.get(s[c], 0) + 1
            tMap[t[c]] = tMap.get(t[c], 0) + 1

        return sMap == tMap